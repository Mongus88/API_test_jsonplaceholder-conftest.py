from clients.base_client import BaseClient

class PostClient(BaseClient):
    def __init__(self, session, base_url):
        super().__init__(session, base_url, endpoint="posts")

    def get_post(self, post_id):
        response = self.session.get(f"{self.url}/{post_id}")
        return self.log_and_return(response)

    def create_post(self, title, body, user_id):
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = self.session.post(self.url, json=payload)
        return self.log_and_return(response)

    def edit_post(self, post_id, title, body, user_id):
        payload = {
            "id" : post_id,
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = self.session.put(f"{self.url}/{post_id}", json=payload)
        return self.log_and_return(response)
