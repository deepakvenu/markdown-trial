import subprocess
import os

def pdf_to_markdown(pdf_path, output_dir="output"):
    """
    Convert a PDF file to Markdown using Marker API.

    Args:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Directory to save the Markdown file.

    Returns:
        str: Path to the converted Markdown file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the command for Marker
    command = [
        "python",  # Using Python command
        "/Users/deepakvenugopal/pdf-trials/marker-trial/.venv/bin/marker_single",  # Full path to marker script
        pdf_path,  # Input PDF
        "--output_format", "markdown",  # Specify Markdown output
        "--output_dir", output_dir  # Specify output directory
    ]

    try:
        # Run the command
        subprocess.run(command, check=True)
        # Output Markdown file
        output_file = os.path.join(output_dir, os.path.basename(pdf_path).replace(".pdf", ".md"))
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error while converting PDF to Markdown: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    pdf_file = "docs/pdf/R1-2112947-accepted-all-changes.pdf"  # Path to your PDF
    output_directory = "docs/markdown_output/accepted-all-changes"
    markdown_file = pdf_to_markdown(pdf_file, output_directory)

    if markdown_file:
        print(f"Markdown file created: {markdown_file}")
    else:
        print("Failed to convert PDF to Markdown.")