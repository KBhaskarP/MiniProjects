# from flask import Flask,jsonify
# import func as f

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/fun/<int:a>')
# def iseven(a):
#     if a%2==0:
#         result={
#             "Number":a,
#             "Even":True,
#             "Staus":"Done",
#             "IP":"123.124.125.69"
#         }
#     else:
#         result={
#             "Number":a,
#             "Even":False,
#             "Staus":"Done",
#             "IP":"123.124.125.69"
#         }
#     return jsonify(result)


# if __name__=="__main__":
#     app.run(debug=True)