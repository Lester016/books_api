from flask import Flask, request, jsonify

app = Flask(__name__)

books_lists = [
  {
    "id": 0,
    "author": "Lester De Guzman",
    "language": "Tagalog",
    "title": "The Life of Lester De Guzman"
  },
  {
    "id": 1,
    "author": "Mark Manson",
    "language": "English",
    "title": "Models, Attract Women through honesty"
  },
  {
    "id": 2,
    "author": "Charles Duhigg",
    "language": "English",
    "title": "The Power of Habit"
  },
  {
    "id": 3,
    "author": "Niccolo Machiavelli",
    "language": "English",
    "title": "The Prince"
  },
]


@app.route("/books", methods=["GET", "POST"])
def books():
  if request.method == "GET":
    if len(books_lists) > 0:
      return jsonify(books_lists)
    else:
      "Nothing found", 404

  if request.method == "POST":
    new_author = request.form['author']
    new_lang = request.form['language']
    new_title = request.form['title']
    iD = books_lists[-1]['id'] + 1

    new_object = {
      'id': iD,
      'author': new_author,
      "language": new_lang,
      'title': new_title,
    }
    books_lists.append(new_object)
    return jsonify(books_lists), 201


@app.route('/book/<int:id>', methods=["GET", "PUT", "DELETE"])
def single_book(id):
  if request.method == "GET":
    for book in books_lists:
      if(book['id'] == id):
        return jsonify(book)
    "Nothing found", 404

  if request.method == "PUT":
    for book in books_lists:
      if(book['id'] == id):
        book['author'] = request.form['author']
        book['language'] = request.form['language']
        book['title'] = request.form['title']

        updated_book = {
          'id': id,
          'author': book['author'],
          'language': book['language'],
          'title': book['title']
        }

        return jsonify(updated_book)

  if request.method == "DELETE":
    for index, book in enumerate(books_lists):
      if book['id'] == id:
        books_lists.pop(index)
        return jsonify(books_lists)


if __name__ == "__main__":
  app.run()
