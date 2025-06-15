#!/bin/bash

# Credentials
USERNAME="Vaibhav Pandey"
PASSWORD="passwd#123"

# API URLs
LOGIN_URL="http://127.0.0.1:3100/api/login"
BOOKS_URL="http://127.0.0.1:3100/api/books"



## Login and get token
#echo "Logging in and retrieving token..."
#RESPONSE=$(curl -s -X POST $LOGIN_URL \
#-H "Content-Type: application/json" \
#-d "{\"username\":\"$USERNAME\", \"password\":\"$PASSWORD\"}")
#
## Extract token using jq
#ACCESS_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')
#
## Check if token was successfully retrieved
#if [ -z "$ACCESS_TOKEN" ]; then
#  echo "Failed to retrieve token. Response was:"
#  echo "$RESPONSE"
#  exit 1
#fi
#
#echo "Access token successfully retrieved."
#
## Function to add a book
#add_book() {
#  TITLE=$1
#  AUTHOR=$2
#  GENRE=$3
#
#  curl -s -X POST $BOOKS_URL \
#  -H "Content-Type: application/json" \
#  -H "Authorization: Bearer $ACCESS_TOKEN" \
#  -d "{\"title\":\"$TITLE\", \"author\":\"$AUTHOR\", \"genre\":\"$GENRE\"}" \
#  && echo "Added: $TITLE"
#}
#
## Adding books
#echo "Adding books..."
#add_book "Harry Potter and the Sorcerer's Stone" "J.K. Rowling" "Fantasy"
#add_book "Harry Potter and the Chamber of Secrets" "J.K. Rowling" "Fantasy"
#add_book "The Hobbit" "J.R.R. Tolkien" "Fantasy"
#add_book "The Lord of the Rings" "J.R.R. Tolkien" "Fantasy"
#add_book "The Da Vinci Code" "Dan Brown" "Thriller"
#add_book "Angels & Demons" "Dan Brown" "Thriller"
#add_book "The Alchemist" "Paulo Coelho" "Fiction"
#add_book "To Kill a Mockingbird" "Harper Lee" "Classic"
#add_book "1984" "George Orwell" "Dystopian"
#add_book "The Great Gatsby" "F. Scott Fitzgerald" "Classic"
#add_book "Pride and Prejudice" "Jane Austen" "Classic"
#add_book "The Catcher in the Rye" "J.D. Salinger" "Classic"
#add_book "The Chronicles of Narnia" "C.S. Lewis" "Fantasy"
#add_book "A Game of Thrones" "George R.R. Martin" "Fantasy"
#add_book "The Hunger Games" "Suzanne Collins" "Dystopian"
#add_book "The Girl with the Dragon Tattoo" "Stieg Larsson" "Mystery"
#add_book "The Shining" "Stephen King" "Horror"
#add_book "The Fault in Our Stars" "John Green" "Romance"
#add_book "Gone Girl" "Gillian Flynn" "Thriller"
#add_book "The Kite Runner" "Khaled Hosseini" "Drama"

#echo "All books added successfully."
