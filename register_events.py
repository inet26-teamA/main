import pandas as pd

file_path = 'data_file/registered_events.xlsx'  # 既存のExcelファイルのパス

def add_events(address, date, time):
    df = pd.read_excel(file_path)

    new_event = {'住所': address, '開催日時': date, '開催時間': time}
    df = df._append(new_event, ignore_index=True)

    # Excelファイルに上書き保存
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer :
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    print(f"新しいイベントが追加され、{file_path}に保存されました。")

add_events('b', '12/12', '10:00')

def read_events(col):
    df = pd.read_excel('data_file/registered_events.xlsx', sheet_name='Sheet1')

    read_list = df[col].tolist()
    
    return read_list

print(read_events('住所'))