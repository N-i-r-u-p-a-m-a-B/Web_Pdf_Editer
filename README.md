# PDF to Editable HTML Converter with Export

This project provides a web-based application to convert PDF documents into editable HTML content using TinyMCE, a rich text editor. It also includes functionality to export the edited HTML back to a PDF file.

## Features

* **PDF Upload:** Users can upload PDF files through a simple web interface.
* **PDF to HTML Conversion:** The uploaded PDF is converted into HTML content using the `fitz` (PyMuPDF) library.
* **Editable HTML with TinyMCE:** The converted HTML is displayed in a TinyMCE editor, allowing users to edit the content.
* **HTML to PDF Export:** Users can export the edited HTML content back to a PDF file using the `weasyprint` library.

## Technologies Used

* **Python:** Backend logic and server-side processing.
* **Flask:** Web framework for handling HTTP requests and responses.
* **PyMuPDF (fitz):** Library for PDF processing and HTML conversion.
* **WeasyPrint:** Library for HTML to PDF conversion.
* **TinyMCE:** Rich text editor for editing HTML content.
* **HTML/CSS/JavaScript:** Frontend development.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone [repository_url]
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```

5.  **Open in Browser:**
    * Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Requirements

* Python 3.6 or higher
* pip (Python package installer)

## Dependencies

* Flask
* PyMuPDF (fitz)
* WeasyPrint

## Usage

1.  **Upload PDF:** Click the "Choose File" button to select a PDF file.
2.  **Edit HTML:** The PDF content will be converted to HTML and displayed in the TinyMCE editor. Edit the content as needed.
3.  **Export PDF:** Click the "Export PDF" button to download the edited content as a PDF file.

## Notes

* PDF to HTML conversion may not be perfect, especially for complex layouts.
* The appearance of the exported PDF may vary depending on the complexity of the HTML and the capabilities of WeasyPrint.
* Browser extensions may interfere with the TinyMCE script loading. If you encounter errors, disable browser extensions.

## Future Improvements

* Improve layout fidelity during PDF to HTML conversion.
* Add more advanced editing features to TinyMCE.
* Implement user authentication and file storage.
* Enhance error handling and provide more informative error messages.
* Add more extensive styling options.
