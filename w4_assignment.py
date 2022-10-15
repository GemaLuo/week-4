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

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#登入：使用POST方法
@app.route("/signin", methods=["POST"])
def signin():
    if request.form["username"]=="test" and request.form["password"]=="test": #確認帳密是否為test，而非是否有相等！
        session["user"]=request.form["username"] #使用者登入狀態
        return redirect ("http://127.0.0.1:3000/member")
    elif request.form["username"]=="" or request.form["password"]=="":
        return redirect ("http://127.0.0.1:3000/error?message=nothing")
    else:
        return redirect ("http://127.0.0.1:3000/error?message=wrong")

#成功進入會員頁
#未登入時導向首頁
@app.route("/member") #不需要檢查帳密！僅確認登入狀態！
def member():
    if "user" in session: #驗證成功，進入會員頁
        return render_template("member.html")
    else:
        return redirect("/")


#登出會員頁面，回到首頁
#登出時刪除紀錄
@app.route("/signout")
def signout():
    session.pop("user", None) #刪除session
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
