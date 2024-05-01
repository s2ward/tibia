import json

# Load the original books.json file
with open('main/api/books.json', 'r', encoding='utf-8') as file:
    books_data = json.load(file)

# Extract the "name", "img", and "type" fields
books_img_data = [
    {
        "name": book["name"].replace(" ", "_"),
        "img": [img.replace(" ", "_") for img in book["img"]],
        "type": book["type"]
    }
    for book in books_data
]

# Save the extracted data to books_img.json
with open('main/api/book-images.json', 'w', encoding='utf-8') as file:
    json.dump(books_img_data, file, indent=4)

