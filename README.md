# Flix API

Flix API is a RESTful API designed to provide information about movies, series, and actors. It allows users to fetch
details about their favorite films, TV shows, and celebrities, offering a wide range of endpoints to interact with the
database.

### Features

- Retrieve details of movies and series.
- Get information about actors and actresses.
- Search for movies, series, and people.
- Supports pagination for large data sets.
- Provides filtering options to refine search results.

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- SQLLite (for data storage)

### Endpoints

Here are some of the main endpoints provided by the API:

- GET /movies: Retrieve a list of movies.
- GET /movies/{id}: Retrieve details of a specific movie by ID.
- POST /movies: Create a new movie.
- PUT /movies/{id}: Update details of a specific movie by ID.
- DELETE /movies/{id}: Delete a specific movie by ID.
- GET /genre: Retrieve a list of series.
- GET /genre/{id}: Retrieve details of a specific series by ID.
- POST /genre: Create a new series.
- PUT /genre/{id}: Update details of a specific series by ID.
- DELETE /genre/{id}: Delete a specific series by ID
- GET /actors: Retrieve a list of actors.
- GET /actors/{id}: Retrieve details of a specific actor by ID.
- POST /actors: Create a new actor.
- PUT /actors/{id}: Update details of a specific actor by ID.
- DELETE /actors/{id}: Delete a specific actor by ID.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

