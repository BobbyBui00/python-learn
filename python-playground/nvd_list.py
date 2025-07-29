import requests
import json
import xlsxwriter
import datetime

def write_to_excel(json_obj):
    row_headers = ['CVE Id', 'Source Identifier', 'Published', 'Last Modified', 'Vulnerability Status', 'CVE Tags', 'descriptions', 'references']

    workbook = xlsxwriter.Workbook("vulnerabilities.xlsx")
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({ "bold": True })

    #Add header column
    worksheet.write_row(0, 0, tuple(row_headers), bold)

    row = 2
    for i in range(0, len(json_obj)):
        cve = json_obj[i].get('cve')
        worksheet.write_row(row, 0, tuple([str(cve.get('id')), str(cve.get('sourceIdentifier')), str(cve.get('published')), str(cve.get('lastModified')), str(cve.get('vulnStatus')), str(cve.get('cveTags')), str(cve.get('descriptions')[0].get('value')), str(cve.get('references'))]))
        row+=1

    workbook.close()

# res = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity=CRITICAL")
now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000')
beginning_of_month = datetime.datetime.now().replace(day=1).strftime('%Y-%m-%dT%H:%M:%S.000')

res = requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate={beginning_of_month}&pubEndDate={now}")
print(res)
# res = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate='{}'&pubEndDate='{}'".format(beginning_of_month, now))
# json_formatted = json.dumps(res.json(), indent=2)
# print(json_formatted)
write_to_excel(res.json().get('vulnerabilities'))