import xml.etree.ElementTree as ET
import json
import csv

def convert_xml_to_jsonl_csv(xml_file, jsonl_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    jsonl_data = []
    csv_data = []

    for schema in root.findall('schema'):
        text = schema.find('text')
        txt1 = text.find('txt1').text
        pron = text.find('pron').text
        txt2 = text.find('txt2').text

        quote = schema.find('quote')
        quote1 = quote.find('quote1').text
        quote_pron = quote.find('pron').text
        quote2 = quote.find('quote2').text

        answers = [answer.text for answer in schema.find('answers')]
        correct_answer = schema.find('correctAnswer').text
        source = schema.find('source').text

        data = {
            'text': f"{txt1} {pron} {txt2}",
            'quote': f"{quote1} {quote_pron} {quote2}",
            'answers': answers,
            'correctAnswer': correct_answer,
            'source': source
        }

        jsonl_data.append(data)
        csv_data.append([txt1, pron, txt2, quote1, quote_pron, quote2, ','.join(answers), correct_answer, source])

    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for item in jsonl_data:
            f.write(json.dumps(item) + '\n')

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['txt1', 'pron', 'txt2', 'quote1', 'quote_pron', 'quote2', 'answers', 'correctAnswer', 'source'])
        writer.writerows(csv_data)

# Example usage
convert_xml_to_jsonl_csv('input.xml', 'output.jsonl', 'output.csv')
