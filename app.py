import pandas as pd
from flask import Flask, request
import requests
app = Flask(__name__)
# def coon_pool_to_google_spreadsheet(sheet_id):
@app.route('/add_users')
def add_users():
    url = 'https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174'

# sheet_id = '1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU'
# url = coon_pool_to_google_spreadsheet(sheet_id=sheet_id)
    df = pd.read_csv(url)
    
    for i in range(len(df)):
        first_name = df.iloc[i]['first_name']
        email = df.iloc[i]['first_name'][0:3]
        email = email.lower()
        email = f"{email}{i}@gmail.com"
        password = i

        payload = {
            "name": first_name,
            "email": email,
            "password": password
        }

        API_ENDPOINT = 'http://0.0.0.0:8000/v1/register'
        response = requests.post(url = API_ENDPOINT, data=payload)        
    return {'status': 'users added succesfully'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 8001, debug=True)


 