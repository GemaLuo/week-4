from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key="test"
user={"test":"test"}

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#登入：使用POST方法
@app.route("/signin", methods=["POST"])
def signin():
    if request.form["password"]==request.form["username"]: #若密碼test等於帳號test
        session["save"]=request.form["username"]
        return redirect ("http://127.0.0.1:3000/member")
    elif request.form["username"]=="" or request.form["username"]==None:
        session["save"]=None
        return redirect ("http://127.0.0.1:3000/error?message=nothing")
    elif request.form["password"]=="" or request.form["password"]==None:
        session["save"]=None
        return redirect ("http://127.0.0.1:3000/error?message=nothing")
    else:
        session["save"]=None
        return redirect ("http://127.0.0.1:3000/error?message=wrong")

#成功進入會員頁
#未登入時導向首頁
@app.route("/member")
def member():
    if session["save"] in user: #驗證成功，進入會員頁
        return render_template("member.html")
    elif session["save"] not in user:
        return redirect ("http://127.0.0.1:3000/")
    elif session["save"]== "": 
        return redirect("http://127.0.0.1:3000/")
    elif session["save"]== None: 
        return redirect("http://127.0.0.1:3000/")
    else:
        return redirect("http://127.0.0.1.3000/")

#登出會員頁面，回到首頁
@app.route("/signout")
def signout():
    session["save"]= None
    return redirect("http://127.0.0.1:3000/")

#失敗頁面
@app.route("/error")
def error():
    if request.args.get("message")=="nothing":
        return render_template("nothing.html")
    elif request.args.get("message")=="wrong":
        return render_template("error.html")
    else:
        return render_template("error.html")

app.run(port=3000)
