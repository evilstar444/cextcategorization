from app import app

@app.route('/')
def index():
    return 'Flask api started'

if __name__ =='__main__':
    app.run()