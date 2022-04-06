import numpy as np
import app.model as model

from flask import Flask,request,jsonify
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test',mothods=['Get'])

def getResult():
    input = "蔡英文"
    result=model.myPredict(input)
    return jsonify({'result':str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['book']
    
    

    result = model.myPredict(x1)

    return jsonify({'return': str(result)})
     
if __name__ == '__main__':
    app.debug = True
    app.run()