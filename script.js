document.addEventListener('DOMContentLoaded', () => {
    tinymce.init({
        selector: '#editor'
    });

    document.getElementById('pdfUpload').addEventListener('change', async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('pdf', file);

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (data.html) {
            tinymce.activeEditor.setContent(data.html);
        }
    });

    document.getElementById('exportButton').addEventListener('click', async () => {
        const htmlContent = tinymce.activeEditor.getContent();
        const response = await fetch('/export', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ html: htmlContent })
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'edited.pdf';
            a.click();
        }
    });
});