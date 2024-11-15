from python_graphql_client import GraphqlClient

class MovieClient:
    MOVIE_URL = "http://127.0.0.1:3001/graphql"

    def __init__(self) -> None:
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