from django.shortcuts import render
import pandas as pd

def uploadexcel(request):
    context = {}
    context['group2'] = "ExcelSheet"
    if request.method == "POST":
        status = handle_uploaded_file(request.FILES['excel_file'])
        if status == True:
            group2 = pd.read_excel('excelfiles/contact.xlsx')
            try:
                context['excel_data'] = []
                for index, row in group2.iterrows():
                    context['excel_data'].append({'id': row['id'], 'username': row['username']})
                    #print(row['id'], row['username'])
            except:
                context['excel_error'] = "Excel sheet error"
    return render(request, "excel.html", context)

def handle_uploaded_file(f):
    with open('excelfiles/contact.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return True
