from fastapi import FastAPI

app = FastAPI()
BOOKS = [
{ "title" : "Harry Potter" , "Author" : "JK Rowling"},
{ "title" : "All her fault" , "Author" : "Andrea Mara"},
{ "title" : "Neighbour next door" , "Author" : "Andrea Mara"},
]

@app.get("/readbooks/author/{author}")
async def read_books(author: str):
    BOOKS_TO_RETURN = []
    for book in BOOKS:
        if book.get("Author").casefold() == author.casefold():
            BOOKS_TO_RETURN.append(book)
    return BOOKS_TO_RETURN




