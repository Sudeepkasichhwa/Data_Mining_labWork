import fitz
import pandas as pd
import os


def get_path():
    final_path=[]
    path1=input("Enter the path for AI files: ")
    print("Path registered successfully ")
    path2=input("Enter the path for WEB: ")
    print("Path registered successfully ")
    final_path.append(path1)
    final_path.append(path2)
    return final_path


def get_final_dataframe(path,flag):
    df = pd.DataFrame(columns=['text','label'])
    content = []
    for file in os.listdir(path):
        doc = fitz.open(path+'\\'+file)
        content_temp = ''
        for page in range(len(doc)):
            content_temp = content_temp + doc[page].get_text()
            print(content_temp)
    df['text'] = content
    df['label'] = flag
    print(df)
    return df

def get_content_of_pdfs(file_path):
    for path in file_path:
        if '\\AI' in path:
            print('----- AI Files -----')
            print(path)
            df_ai = get_final_dataframe(path,1)
        elif '\\WEB' in path:
            print('---- WEB Files ----')
            print(path)
            df_web = get_final_dataframe(path,0)
    
    df = df_ai.append(df_web)
    return df


def get_content(file_path):
    df = pd.DataFrame(columns = ['text','label'])
    df = get_content_of_pdfs(file_path)
    return df


def generate_dataset():
    file_path = get_path()
    dataset = get_content(file_path)
    dataset.to_csv(dataset.csv)


if __name__=='__main__':
    file_path=get_path()


