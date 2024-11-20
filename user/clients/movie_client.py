from python_graphql_client import GraphqlClient
import os 

class MovieClient:
    """
    Client class for interacting with the Movie service via GraphQL.

    This class allows fetching detailed information about movies, including title,
    rating, and actor details, by querying the Movie GraphQL API.
    """

    def __init__(self) -> None:
        self.MOVIE_URL = str(os.getenv("MOVIE_CLIENT")) + "/graphql"
        self.client = GraphqlClient(self.MOVIE_URL)

    def get_movie_details(self, movie_id):
        """
        Fetches detailed information about a movie by its ID.
        """
        
        query = """
        query getMovieDetails($id: String!) {
            movie_with_id(_id: $id) {
                title
                rating
                actors {
                    firstname
                    lastname
                    birthyear
                }
            }
        }
        """
        variables = {"id": movie_id}
        data = self.client.execute(query=query, variables=variables)    
        return data["data"]["movie_with_id"]