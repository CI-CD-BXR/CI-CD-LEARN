from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"""
    <h1>🎉 CI/CD 部署成功！</h1>
    <p>这个页面是从 GitHub 自动部署到阿里云服务器的。</p>
    <p>当前时间：{now}</p>
    """

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
