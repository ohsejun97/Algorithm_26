# Assignment 02: Complexity Analysis & Performance Report

**Course:** 2026 Algorithm Lecture  
**Topic:** Time Complexity (O(1), O(n), O(n²)) Validation  
**Date:** March 16, 2026  

---

## 1. Complexity Analysis (Deliverable 1)

This project implements three different search strategies to demonstrate how algorithmic complexity affects system performance.

### A. ID Lookup: $O(1)$ (Constant Time)
- **Endpoint:** `/search/id`
- **Theory:** Uses a Python Dictionary (Hash Map). The time required to find an element by its key is independent of the total number of elements ($n$).
- **Implementation:** `products_dict.get(id)` provides direct access.

### B. Name Search: $O(n)$ (Linear Time)
- **Endpoint:** `/search/name`
- **Theory:** Uses a single `for` loop (list comprehension) to scan all products. The execution time grows proportionally with the number of products.
- **Implementation:** `[p for p in products_list if q in p["name"].lower()]`

### C. Duplicate Detection: $O(n^2)$ (Quadratic Time)
- **Endpoint:** `/search/duplicates`
- **Theory:** Uses nested `for` loops to compare every product pair. If the dataset size doubles, the execution time increases fourfold.
- **Implementation:** 
  ```python
  for i in range(n):
      for j in range(i + 1, n):
          if products_list[i]["name"] == products_list[j]["name"]:
              # Comparison logic
  ```

---

## 2. Evidence of Implementation (Deliverable 2)

The backend is built using **FastAPI**. Below are the core snippets demonstrating the complexity differences:

```python
# O(1) Implementation (Dictionary)
@app.get("/search/id")
async def search_by_id(id: int):
    result = products_dict.get(id) # Immediate access
    return {"complexity": "O(1)", "results": [result]}

# O(n^2) Implementation (Nested Loops)
@app.get("/search/duplicates")
async def find_duplicates():
    for i in range(n):
        for j in range(i + 1, n): # Nested loop comparing every pair
            if products_list[i]["name"] == products_list[j]["name"]:
                # Logic to collect duplicates
    return {"complexity": "O(n^2)"}
```

---

## 3. Performance Results & Comparison (Deliverable 3)

Based on actual testing with 1,000 product items, the execution times were measured as follows:

| Search Type | Complexity | Execution Time (ms) | Speed Ratio |
| :--- | :--- | :--- | :--- |
| **ID Lookup** | $O(1)$ | **0.0012 ms** | 1x (Baseline) |
| **Duplicate Search** | $O(n^2)$ | **21.7074 ms** | **~18,089x Slower** |

### Observation:
The $O(n^2)$ algorithm is significantly slower even with a small dataset of 1,000 items. While 21ms is still fast for a human, if the dataset grows to 100,000 items, the $O(n^2)$ search would take hours, whereas the $O(1)$ search would still take less than 1ms.

---

## 4. Load Testing Analysis (Locust)

Using **Locust**, multiple virtual users were simulated to stress the server.

- **Findings:**
    - Frequent calls to `/search/duplicates` caused a sharp spike in CPU usage.
    - As concurrent users increased, the response time for the $O(n^2)$ endpoint degraded exponentially.
    - The $O(1)$ endpoint maintained stable response times regardless of the load, proving its scalability.

---

## 5. Conclusion (Ideal Solution)

To optimize the $O(n^2)$ duplicate detection to $O(n)$:
1. Use a **Hash Set** or **Dictionary** to track names already seen while iterating through the list once.
2. This would reduce the comparison count from $500,000$ down to $1,000$, making the "Duplicates" search as efficient as a linear scan.

---

## 6. How to Reproduce (Testing Guide)

To verify the performance results, follow these steps:

### 1. Start the FastAPI Server (Port 8000)
```bash
cd Assignments/week2
python app.py
```
- The server will run at `http://localhost:8000`.

### 2. Run the Load Test (Port 8089)
```bash
# In a new terminal
locust -f locustfile.py
```
- Open your browser and go to `http://localhost:8089`.
- **Crucial Step:** In the **Host** field of the Locust web interface, you must enter: `http://localhost:8000`.
- Alternatively, run from the command line with the host pre-defined:
  ```bash
  locust -f locustfile.py --host=http://localhost:8000
  ```

---
*End of Report*
