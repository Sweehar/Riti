from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/success/<int:score>')
def success(score):
    res='pass' if score>=50 else 'fail'
    return render_template('res.html',res=res)


@app.route('/pass/<int:score>')
def Pass(score):
    return "Person has passed and scored " + str(score)

@app.route('/fail/<int:score>')
def Fail(score):
    return "Person has failed and scored " + str(score)

@app.route('/result/<int:score>')
def results(score):
    result = "Pass" if score >= 50 else "Fail"
    return redirect(url_for(result, score=score))

@app.route('/submit',methods=['POST','GET'])
def submit():
      total_score=0
      if request.method=='POST':
          science=float(request.form['science'])
          math=float(request.form['math'])
          c=float(request.form['c'])
          ds=float(request.form['ds'])
          total_score=(science+math+c+ds)/4
      
      if total_score>=50:
         res="success"  
      else:
          res="fail"  
      return redirect(url_for(res,score=total_score))     
         
if __name__ == '__main__':
    app.run(debug=True)



