from flask import Flask,request, jsonify
app =Flask(__name__)
@app.route("/Fact/<int:num>",methods=['GET'])
def factorial(num):
    factorial = 1 
    for i in range(1,num +1):
        factorial = factorial*i
        
    return jsonify({'input' : num ,'output' : factorial })

if __name__ == '__main__':
    app.run(port = 4000,debug=True)
