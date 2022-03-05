from typing import IO
from urllib.request import urlopen, Request
import tempfile
import re

import PyPDF2
from PyPDF2.utils import PdfReadError


def fetch_incidents(url: str) -> list:
    """Returns the extracted raw incidents data (unparsed) from all pages of the given URL"""

    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        with urlopen(Request(url, headers=headers)) as resp:
            with tempfile.TemporaryFile() as fp:
                fp.write(resp.read())
                fp.seek(0)

                return extract_incidents(fp)
    except Exception:
        print(f'Could not retrieve: {url}')
        return None


def extract_incidents(temp_file: IO[bytes]) -> list:
    """Returns an array of page-wise extracted unformatted string from the given PDF BytesIO object"""

    try:
        pdf_reader = PyPDF2.pdf.PdfFileReader(temp_file)
        pages_count = pdf_reader.numPages

        pages_text = ""
        for i in range(pages_count):
            page_text = pdf_reader.getPage(i).extractText()
            pages_text += page_text

        temp_file.close()

        pages_text = re.sub(
            'Date / Time\nIncident Number\nLocation\nNature\nIncident ORI\n',
            '',
            pages_text)
        pages_text = re.sub(
            r'NORMAN POLICE DEPARTMENT\nDaily Incident Summary \(Public\)\n',
            '',
            pages_text)
        pages_text = re.sub(
            r'\n(\d+/\d+/\d{4}.\d+:\d\d)',
            lambda x: f'\n;;{x.group(1)}',
            pages_text)
        pages_text = re.sub(
            r'([\w,\.;#\'<>&\(\) /-]*) \n([\w,\.;#\'<>&\(\) /-]*)',
            lambda x: f'{x.group(1)} {x.group(2)}',
            pages_text)
        pages_text += ';;'

        data = re.findall(
            r'(\d+/\d+/\d{4}.\d+:\d\d)\n(\d{4}-\d{8})\n([\w,\.;#\'<>&\(\) /-]*)\n([\w /]*)\n([\w /]*)\n;;',
            pages_text)
        data += re.findall(
            r'(\d+/\d+/\d{4}.\d+:\d\d)\n(\d{4}-\d{8})()()\n([\w /]*)\n;;',
            pages_text)

        return data
    except PdfReadError:
        print("Invalid PDF file")
        return None
