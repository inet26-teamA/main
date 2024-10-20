"""
・イベントを登録する
add_events('年', '月', '日', 'イベント名', '住所')

・1列だけを取得する
get_events('列名') #get_events('address') で、保存されている住所をすべてリストとして取得

・すべての列を2次元リストとして取得 引数なし
get_all_col()

"""

import pandas as pd

file_path = 'data_file/registered_events.xlsx'  # 既存のExcelファイルのパス

def add_events(year: int, month: int, date: int, event_name: str, address: str): #イベントの追加
    df = pd.read_excel(file_path)
    new_event = {'年': year, '月': month, '日': date, 'イベント名': event_name, '住所': address}
    df = df._append(new_event, ignore_index=True)

    # Excelファイルに上書き保存
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer :
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    print(f"新しいイベントが追加され、{file_path}に保存されました。")


def get_events(col): #イベントの取得 
    df = pd.read_excel('data_file/registered_events.xlsx', sheet_name='Sheet1')

    read_list = df[col].tolist()
    
    return read_list

def get_all_col():
    df = pd.read_excel('data_file/registered_events.xlsx', sheet_name='Sheet1')
    return df.values.tolist()
    #return df.T.values.tolist() #出力を転置する

# add_events(2024, 10, 20, 'newevent1', 'tokyo')
# add_events(2024, 10, 21, 'newevent2', 'kanda')

print(get_all_col())