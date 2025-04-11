from flask import Flask
import json
app = Flask(__name__)
@app.route('/alkuluku/<num>')
def alkuluku(num):
    global testi
    testi = True
    num = int(num)
    try:
        for l in range(2,num-1):
            if num%l==0:
                testi = False
        txt = {
            'Number':num,
            'isPrime':testi
        }

    except ValueError:
        txt = {
            'teksti':'jotain meni pieleen'
        }
    txtjson = json.dumps(txt)
    return txtjson

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)