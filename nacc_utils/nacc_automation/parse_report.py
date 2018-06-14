# -*- encoding: utf-8 -*-
import sys
import os
import xml.etree.ElementTree as ET
import ConfigParser
from jinja2 import Environment

import send_email as sm


def read_config(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config


def generate_report_csv(input_file):

    cmd = 'pdf2txt.py -A -o out.xml ' + input_file
    os.system(cmd)
    filename = 'out.xml'

    tree = ET.parse(filename)
    pages = tree.getroot()
    final_result = {}
    for iter in pages[0].findall('textbox'):
        # ADC IDs Total
        if iter.attrib['id'] == '35':
            result = []
            for t_iter in iter.findall('textline')[-1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['ADC IDs Total'] = ''.join(result)

        # ADC Percentage
        if iter.attrib['id'] == '33':
            result = []
            for t_iter in iter.findall('textline')[-1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['ADC Percentage'] = ''.join(result)

        # Autopsies
        if iter.attrib['id'] == '36':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['Autopsies'] = ''.join(result)

        # Autopsies Percentage
        if iter.attrib['id'] == '34':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['Autopsies Percentage'] = ''.join(result)

        # NP Forms
        if iter.attrib['id'] == '36':
            result = []
            for t_iter in iter.findall('textline')[1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['NP Forms'] = ''.join(result)

        # 6+
        if iter.attrib['id'] == '8':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['6+'] = ''.join(result)

        # <6
        if iter.attrib['id'] == '4':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['<6'] = ''.join(result)

        # Date Entered
        if iter.attrib['id'] == '0':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            result = str.replace(''.join(result), 'Asof', '')
            final_result['Date Entered'] = result

    print final_result

    page2_result = {}
    expected = {}
    completed = {}
    in_person = {}
    telephone = {}
    missed = {}

    # Cumulative missed result
    for iter in pages[1].findall('textbox'):
        # First Column
        if iter.attrib['id'] == '3':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            expected['IV'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            completed['IV'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[2].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            in_person['IV'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[3].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            telephone['IV'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[4].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            missed['IV'] = ''.join(result)

        # Second column
        if iter.attrib['id'] == '4':
            result = []
            for t_iter in iter.findall('textline')[2].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            expected['F1'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[3].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            completed['F1'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[4].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            in_person['F1'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[5].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            telephone['F1'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[6].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            missed['F1'] = ''.join(result)

        # Third column
        if iter.attrib['id'] == '6':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            expected['F2'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            completed['F2'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[2].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            in_person['F2'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[3].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            telephone['F2'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[4].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            missed['F2'] = ''.join(result)

    page2_result = {'Expected': expected, 'Completed': completed, 'In-Person': in_person, 'Telephone': telephone, 'Missed': missed}
    print page2_result

    page3_result = {}

    # Imaging stored at NACC
    for iter in pages[2].findall('textbox'):
        # First Column
        if iter.attrib['id'] == '25':
            result = []
            for t_iter in iter.findall('textline')[1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            page3_result['Structural MRI'] = ''.join(result)

            result = []
            for t_iter in iter.findall('textline')[2].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            page3_result['Amyloid PET'] = ''.join(result)

    print page3_result


    TEMPLATE = """
    <html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
    <p>To view today's or any previous reports, please go here:</p>
    <p>https://drive.google.com/drive/folders/1f9LmoC_4SiJBhbLd8ZqHA9BeajinmByr</p>
    <p>Summary data can be found here:</p>
    <p>https://docs.google.com/spreadsheets/d/11C-xzunVZnbT_beAHh870S3YtPHjH6OTM0we7oe2o0s/edit#gid=0</p>
    <table style="width:100%"; border="1">
    <!-- table header -->
    {% if final_result %}
        <tr>
            {% for key in final_result.keys() %}
                <td> {{ key }} </td>
            {% endfor %}
        </tr>
    <!-- table rows -->
        <tr>
            {% for value in final_result.values() %}
                <td> {{ value }} </td>
            {% endfor %}
        </tr>
    {% endif %}
    </table>
    <br>
    <br>
    <br>
    <table style="width:100%"; border="1">
    <caption>Cumulative missed visit rate</caption>
    <thead>
    <tr>
        <th scope="col"></th>
        <th scope="col">IV</th>
        <th scope="col">F1</th>
        <th scope="col">F2</th>
        <th scope="col">Date Recorded</th>
    </tr>
    </thead>
    <tbody>
        <tr>
        <th scope="row">Expected(n)</th>
        <td>{{ page2_result['Expected']['IV'] }}</td>
        <td>{{ page2_result['Expected']['F1'] }}</td>
        <td>{{ page2_result['Expected']['F2'] }}</td>
        <td>{{ final_result['Date Entered'] }}</td>
        </tr>
        <tr>
        <th scope="row">Completed(n)</th>
        <td>{{ page2_result['Completed']['IV'] }}</td>
        <td>{{ page2_result['Completed']['F1'] }}</td>
        <td>{{ page2_result['Completed']['F2'] }}</td>
        <td></td>
        </tr>
        <tr>
        <th scope="row">In-Person(n)</th>
        <td>{{ page2_result['In-Person']['IV'] }}</td>
        <td>{{ page2_result['In-Person']['F1'] }}</td>
        <td>{{ page2_result['In-Person']['F2'] }}</td>
        <td></td>
        </tr>
        <tr>
        <th scope="row">Telephone(n)</th>
        <td>{{ page2_result['Telephone']['IV'] }}</td>
        <td>{{ page2_result['Telephone']['F1'] }}</td>
        <td>{{ page2_result['Telephone']['F2'] }}</td>
        <td></td>
        </tr>
        <tr>
        <th scope="row">Missed(%)</th>
        <td>{{ page2_result['Missed']['IV'] }}</td>
        <td>{{ page2_result['Missed']['F1'] }}</td>
        <td>{{ page2_result['Missed']['F2'] }}</td>
        <td></td>
        </tr>
    </tbody>
    </table>
    <br>
    <br>
    <br>
    <table style="width:100%"; border="1">
    <caption>Imaging stored at NACC</caption>
    <thead>
    <tr>
        <th scope="col">Type</th>
        <th scope="col">Subjects(n)</th>
        <th scope="col">Date Recorded</th>
    </tr>
    </thead>
    <tbody>
        <tr>
        <th scope="row">Structural MRI</th>
        <td>{{ page3_result['Structural MRI'] }}</td>
        <td>{{ final_result['Date Entered'] }}</td>
        </tr>
        <tr>
        <th scope="row">Amyloid PET)</th>
        <td>{{ page3_result['Amyloid PET'] }}</td>
        <td></td>
        </tr>
    </tbody>
    </table>

    </body>
    </html>
    """  # Our HTML Template

    # Create a text/html message from a rendered template
    msg = Environment().from_string(TEMPLATE).render(
            title='UDS REPORT',
            final_result=final_result,
            page2_result=page2_result,
            page3_result=page3_result
        )

    sm.send_email(subject='UDS REPORT', message=msg)


def main(argc):
    input_file = argc
    generate_report_csv(input_file)


if __name__ == '__main__':
    main(sys.argv[1])
