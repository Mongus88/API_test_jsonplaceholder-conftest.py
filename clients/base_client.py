class BaseClient:
    def __init__(self, session, base_url, endpoint):
        self.session = session
        self.url = f"{base_url}/{endpoint}"

    def log_and_return(self, response):
        duration = response.elapsed.total_seconds()
        size = len(response.content)

        print(f"\n{'=' * 20} API CALL: {self.__class__.__name__} {'=' * 20}")
        print(f"URL:    {response.url}\n")
        print(f"TIME:    {duration:.3f} s | SIZE: {size} Bytes\n")
        print(f"BODY:   {response.text}\n")
        print(f"{'=' * 60}")

        return response
