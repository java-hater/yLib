class Book {
  final String isbn;
  final String author;
  final String pages;
  final String publisher;
  final String publish_date;
  final String cover_url;

  Book({
    required this.isbn,
    required this.author,
    required this.pages,
    required this.publisher,
    required this.publish_date,
    required this.cover_url
  })
}

/**
 * "isbn": isbn,
        "title": data["title"],
        "author": data["authors"][0]["name"],
        "pages": data["pagination"],
        "publisher": data["publishers"][0]["name"],
        "publish_date": data["publish_date"],
        "cover_url": data["cover"]
 */
