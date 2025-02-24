import logging
from weasyprint import HTML
import os

logging.basicConfig(level=logging.DEBUG)


def generate_pdf(html_file, output_pdf):
    """Generates a PDF from an HTML file."""
    try:
        if not os.path.exists(html_file):
            raise FileNotFoundError(f"HTML file {html_file} not found.")

        # Create an HTML object and generate the PDF
        html = HTML(filename=html_file)
        html.write_pdf(output_pdf)
        print(f"PDF generated successfully: {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    html_file = "template_cv2.html"  # Ensure this HTML file exists
    output_pdf = "data_scientist_resume.pdf"
    generate_pdf(html_file, output_pdf)
