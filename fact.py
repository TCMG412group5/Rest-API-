from flask import Flask,request, jsonify
app =Flask(__name__)
@app.route("/Fact/<int:num>",methods=['GET'])
def factorial(num):
    factorial = 1 
    for i in range(1,num +1):
        factorial = factorial*i
        
    return jsonify({'input' : num ,'output' : factorial })

@app.route("/Fib/<int:num>",methods=['GET'])
def fib(num):
    l = [0,1] 
    if num < len(l):
        return jsonify ({"Input": num, "output" : l})
    else:
        for i in range (len(l), num+1):
                sum=l[i-1] +l[i-2]
                l.append(sum)
            
    return jsonify({"input" : num, "output" : l})
if __name__ == '__main__':
    app.run(port = 4000,debug=True)

