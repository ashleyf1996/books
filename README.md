# Books API Project

Project 1 – Simple FastAPI Book Lookup Service

This project is a small introductory FastAPI application that demonstrates how to build a basic API endpoint and work with in-memory data.

The application exposes a single endpoint that lets users search for books by author. A predefined list of books is stored in memory, and when a request is made to the API, it filters and returns all books written by the specified author.

Features

Built using FastAPI, a modern, fast Python web framework

Stores sample book data in an in-memory list

Provides a dynamic route to fetch books by author

Case-insensitive matching for user convenience

Simple, lightweight, and ideal as a beginner FastAPI assignment

Endpoint
GET /readbooks/author/{author}

Returns:
A list of books written by the given author.
