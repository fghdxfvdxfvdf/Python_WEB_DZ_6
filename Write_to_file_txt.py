import os


file_path = 'main.txt'

def file_txt_exist():
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('')
          
def record_data_in_txt(res):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(res)
        f.write('\n')

# file_txt_exist()
# record_data_in_txt('f_1: qwerty')
# record_data_in_txt('f_2: 15988')
# record_data_in_txt('f_3: 879456213qwertyu')
# record_data_in_txt('f_4: +++++++')