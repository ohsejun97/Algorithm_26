from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

app = FastAPI()

# static 폴더 마운트 (CSS, JS 파일 서빙용)
app.mount("/static", StaticFiles(directory="static"), name="static")

class CompareRequest(BaseModel):
    text_a: str
    text_b: str

def get_lcs(a, b):
    m, n = len(a), len(b)
    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # 백트래킹을 통한 LCS 문자열 및 Diff 생성
    lcs_str = []
    diff = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs_str.append(a[i-1])
            diff.append({"type": "matched", "char": a[i-1]})
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            diff.append({"type": "removed", "char": a[i-1]})
            i -= 1
        else:
            diff.append({"type": "added", "char": b[j-1]})
            j -= 1
            
    while i > 0:
        diff.append({"type": "removed", "char": a[i-1]})
        i -= 1
    while j > 0:
        diff.append({"type": "added", "char": b[j-1]})
        j -= 1
        
    return dp[m][n], "".join(reversed(lcs_str)), list(reversed(diff))

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/check")
async def check_plagiarism(req: CompareRequest):
    lcs_len, lcs_str, diff = get_lcs(req.text_a, req.text_b)
    max_len = max(len(req.text_a), len(req.text_b))
    similarity = (lcs_len / max_len * 100) if max_len > 0 else 0
    
    return {
        "similarity": round(similarity, 2),
        "lcs_length": lcs_len,
        "lcs_string": lcs_str,
        "diff": diff
    }
