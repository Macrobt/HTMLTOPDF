from playwright.sync_api import sync_playwright

def convert_html_to_pdf(html_file, output_pdf):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Upload the HTML file to the page
        page.goto(f'file:///{html_file}')

        # Wait for all resources to load
        page.wait_for_load_state('networkidle')

        # Save the page as PDF
        page.pdf(path=output_pdf, format='A4', print_background=True)

        browser.close()

# Paths to output HTML and PDF files
html_file = '/path/to/file.html'
output_pdf = '/path/to/output.pdf'


# Conversion
convert_html_to_pdf(html_file, output_pdf)

print(f'Conversion completed. PDF saved as {output_pdf}')
