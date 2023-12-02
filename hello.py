from flask import Flask, jsonify, abort, request
import json


app= Flask (__name__)

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route("/isbns", methods=['GET'])
def get_isbns():
    with open('books.json') as json_data:
        result = []
        data = json.load(json_data)
        for book in data['books']:
            result.append(book['isbn'])

    return jsonify({'isbn': result})

@app.route("/isbns/<isbn>", methods=['GET'])
def get_book_by_isbn(isbn):
    with open('books.json') as json_data:
        data = json.load(json_data)
        for book in data['books']:
            if book['isbn'] == isbn:
                return jsonify(book)

        abort(404)

@app.route("/authors/<expression>", methods=['GET'])
def get_authors_by_title(expression):
    with open('books.json') as json_data:
        data = json.load(json_data)
        matching_authors = set()
        for book in data['books']:
            if expression.lower() in book['title'].lower():
                matching_authors.add(book['author'])

        return jsonify({'authors': list(matching_authors)})
@app.route("/isbns/<isbn>", methods=['PUT'])
def update_publisher(isbn):
    new_publisher = request.args.get('publisher')


    for book in data['books']:
        if book['isbn'] == isbn:

            book['publisher'] = new_publisher


            return jsonify({'message': f'Wydawca książki o ISBN {isbn} został zaktualizowany na {new_publisher}.'})


    abort(404)



if __name__ == '__main__':
    app.run(debug=True)
