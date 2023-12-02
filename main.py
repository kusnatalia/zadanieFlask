from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('books.json') as json_data:
  result = []
  data = json.load(json_data)
  for book in data['books']:
    result.append(book['isbn'])

@app.route("/isbn", methods=['GET'])
def get_isbns():
    isbn_list = [book["isbn"] for book in result]
    print(isbn_list)
    #return(isbn_list)
    return ({"isbn_list"})

if __name__ == '__main__':
    app.run(debug=True)







