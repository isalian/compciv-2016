# Gender Detector Project

Determine the ratio of female-to-male authors on the New York Times Bestsellers list. 

## About the Dataset

Dataset: authors on The New York Times Bestseller List 
Link to the landing page: http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers
Link to dataset: Only available through the NYT Books API 

## Description of Data Fields

### asterisk

Contains an __integer__: if the integer value is `1`, the book's sales are highly similar to the one above it on the list. Otherwise, the value is `0`.

### author

Contains a __string__ with the author's name, which would need wrangling to pull out the first name. 

### bestsellers_date

Contains an __integer__ corresponding to the date for all books on this specific list. 

### contributor

Contains a __list__ of all contributors and their roles (e.g. author, illustrator, translator, etc.)

### contributor_note

Contains a __list__ of all contributors, but excludes the author.

### dagger

Contains an __integer__: if the integer value is `1`, some bookstores have received bulk orders for the book. Otherwise, the value is `0`.

### display_name

Contains a __string__ with the text label for the list used by NYTimes.com

### isbns

Contains a __list__ of ISBN numbers associated with the book.

### published_date

Contains an __integer__ indicating the publication date of the bestseller list on NYTimes.com.

### rank

Contains an __integer__ corresponding to the rank of the bestseller on the particular list on that list's date.

### ranks_history

Contains a __list__ of rank data for the bestseller on all besteller lists and dates.

### review

Contains a __list__ of URLs to Times content about the book, such as the first chapter of text or a book review.