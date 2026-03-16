import time
import random
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 정적 파일 및 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

# 1. 상품 데이터 생성 (1,000개 이상)
# 복잡도 차이를 명확히 하기 위해 중복된 이름의 상품을 의도적으로 포함합니다.
CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
PRODUCT_NAMES = [
    "Smartphone", "Laptop", "Wireless Mouse", "Keyboard", "Monitor", 
    "Headphones", "Coffee Maker", "Toaster", "Air Purifier", "Backpack",
    "T-shirt", "Jeans", "Sneakers", "Watch", "Desk Lamp", "Water Bottle"
]

products_list = []
products_dict = {} # O(1) 조회를 위한 딕셔너리

for i in range(1, 1001):
    # 일부 상품은 이름을 중복되게 생성 (O(n^2) 테스트용)
    # 50개마다 이름이 같은 상품을 생성하도록 함
    name = PRODUCT_NAMES[i % len(PRODUCT_NAMES)]
    price = round(random.uniform(10.0, 500.0), 2)
    category = random.choice(CATEGORIES)
    
    product = {
        "id": i,
        "name": name,
        "category": category,
        "price": price
    }
    products_list.append(product)
    products_dict[i] = product

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. API 엔드포인트 구현

# ID Lookup: O(1) (딕셔너리 활용)
@app.get("/search/id")
async def search_by_id(id: int = Query(...)):
    start_time = time.perf_counter()
    result = products_dict.get(id)
    end_time = time.perf_counter()
    
    execution_time_ms = (end_time - start_time) * 1000
    return {
        "results": [result] if result else [],
        "execution_time_ms": execution_time_ms,
        "complexity": "O(1)"
    }

# Name Search: O(n) (리스트 순차 탐색)
@app.get("/search/name")
async def search_by_name(q: str = Query(...)):
    start_time = time.perf_counter()
    q = q.lower()
    results = [p for p in products_list if q in p["name"].lower()]
    end_time = time.perf_counter()
    
    execution_time_ms = (end_time - start_time) * 1000
    return {
        "results": results,
        "execution_time_ms": execution_time_ms,
        "complexity": "O(n)"
    }

# Duplicate Detection: O(n^2) (이중 루프 활용)
# 같은 이름을 가진 상품 쌍을 모두 찾아냅니다.
@app.get("/search/duplicates")
async def find_duplicates():
    start_time = time.perf_counter()
    duplicates = []
    n = len(products_list)
    
    # 의도적인 O(n^2) 구현: 모든 쌍을 전수 조사
    for i in range(n):
        for j in range(i + 1, n):
            if products_list[i]["name"] == products_list[j]["name"]:
                # 중복 발견 시 간단히 결과에 추가 (너무 많을 수 있으니 상위 50개만 반환)
                if len(duplicates) < 50:
                    duplicates.append({
                        "item1": products_list[i],
                        "item2": products_list[j]
                    })
    
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    
    return {
        "results_count": len(duplicates),
        "results_sample": duplicates,
        "execution_time_ms": execution_time_ms,
        "complexity": "O(n^2)"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
