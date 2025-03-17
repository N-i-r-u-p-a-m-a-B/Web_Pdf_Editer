from flask import Flask, request, jsonify, send_file, render_template, url_for
import fitz
import tempfile
import os
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    print("Upload endpoint hit!")  # Debugging print
    if 'pdf' not in request.files:
        print("No PDF file provided") #debug print
        return jsonify({'error': 'No PDF file provided'}), 400

    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        print("No selected file") #debug print
        return jsonify({'error': 'No selected file'}), 400

    if pdf_file:
        temp_pdf_path = tempfile.mktemp(suffix='.pdf')
        pdf_file.save(temp_pdf_path)

        doc = fitz.open(temp_pdf_path)
        html_content = ""
        for page in doc:
            html_content += page.get_text("xhtml")
        doc.close()
        os.remove(temp_pdf_path)
        print("PDF processed and HTML returned") #debug print
        return jsonify({'html': html_content})

    print("Unknown error") #debug print
    return jsonify({'error': 'Unknown error'}), 500

@app.route('/export', methods=['POST'])
def export_pdf():
    data = request.get_json()
    html_content = data.get('html')

    if not html_content:
        return jsonify({'error': 'No HTML content provided'}), 400

    temp_html_path = tempfile.mktemp(suffix='.html')
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    temp_pdf_path = tempfile.mktemp(suffix='.pdf')
    HTML(temp_html_path).write_pdf(temp_pdf_path)
    os.remove(temp_html_path)

    return send_file(temp_pdf_path, as_attachment=True, download_name='edited.pdf')

if __name__ == '__main__':
    app.run(debug=True)