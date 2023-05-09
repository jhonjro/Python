import zipfile
from io import BytesIO
import base64


def _init_buffer(output, function_name='xlsx'):
    _generate_txt(output, function_name)
    return output


def _generate_txt(output, function_name):
    content = _get_datas_report_txt(output)
    output.write(content.encode())


def _get_datas_report_txt(output):
    content = ""
    for x in range(0, 10):
        content += 'Hello world! %s\n' % x
    return content


def document_to_zip(output):
    output = BytesIO()
    output = _init_buffer(output, function_name='txt')
    output.seek(0)
    return output.read()


def zip(n):
    buffer = BytesIO()
    # buffer = zipfile.ZipFile('C:\\Users\\jhon_\\Documents\\Notes\\archive.zip', 'w')
    zipfile_obj = zipfile.ZipFile(buffer, 'w')
    for j in range(n):
        output_file = BytesIO()
        content = document_to_zip(output_file)
        file_name = 'invoice_to_zip_' + str(j)
        zipfile_obj.writestr(file_name, content, compress_type=zipfile.ZIP_DEFLATED)

    zipfile_obj.close()
    content = buffer.getvalue()
    # base64.encodebytes(content)
    buffer.close()
    return content


zip(5)
