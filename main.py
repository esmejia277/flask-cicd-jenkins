from flask import Flask, jsonify 


app = Flask(__name__)

@app.route("/books")
def get_books():
    books = [
        {
            "id": 1,
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "genre": "Science Fiction",
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian Fiction",
        },
        {
            "id": 3,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "genre": "Fantasy",
        },
    ]

    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)