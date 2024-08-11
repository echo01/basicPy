import datetime
from openpyxl.styles import NamedStyle

def prepareData(source, tagList):
    data = {
        'tagList': tagList,
        'keys': [],
        'sortData': {}
    }
    write_data = []
    for x in source:
        # dateKey = datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        dateKey = x['date']
        data['keys'].append(dateKey)
        if x['nameDevice'] in data['sortData']:
            data['sortData'][x['nameDevice']][dateKey] = x['data']
        else:
            data['sortData'][x['nameDevice']] = {
                dateKey: x['data']
            }

    data['keys'] = sorted(list(set(data['keys'])))

    for x in data['keys']:
        record = [datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ')]
        for device in data['tagList']:
            if x in data['sortData'][device]:
                record.append(data['sortData'][device][x][0]['value'])
            else:
                record.append(0)
        write_data.append(record)
    
    return {
        **data,
        'write_data': write_data
    }


def fill_data(ws, pool):
    row = 2
    for x in pool['write_data']:
        col = 1
        cell = ws.cell(column=col, row=row)
        for d in x:
            cell.value = d
            col += 1
            cell = ws.cell(column=col, row=row)
        row += 1

    return
