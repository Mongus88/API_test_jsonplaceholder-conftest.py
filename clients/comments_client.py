from clients.base_client import BaseClient

class CommentsClient(BaseClient):
    def __init__(self, session, base_url):
        super().__init__(session, base_url, endpoint="comments")

    def get_comments(self, comment_id):
        response = self.session.get(f"{self.url}/{comment_id}")
        return self.log_and_return(response)
