import random
from locust import HttpUser, task, between

class ShoppingMallUser(HttpUser):
    wait_time = between(1, 2)

    @task(5)
    def search_by_id(self):
        """O(1) ID Lookup 테스트"""
        product_id = random.randint(1, 1000)
        self.client.get(f"/search/id?id={product_id}", name="/search/id")

    @task(3)
    def search_by_name(self):
        """O(n) Name Search 테스트"""
        # 임의의 검색어 선택
        queries = ["Smartphone", "Laptop", "Watch", "S", "L"]
        query = random.choice(queries)
        self.client.get(f"/search/name?q={query}", name="/search/name")

    @task(1)
    def find_duplicates(self):
        """O(n²) Duplicate Detection 테스트"""
        self.client.get("/search/duplicates", name="/search/duplicates")
