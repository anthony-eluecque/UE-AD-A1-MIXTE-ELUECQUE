from python_graphql_client import GraphqlClient
import os 

class MovieClient:
    def __init__(self) -> None:
        self.MOVIE_URL = str(os.getenv("MOVIE_CLIENT")) + "/graphql"
        self.client = GraphqlClient(self.MOVIE_URL)

    def get_movie_details(self, movie_id):
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