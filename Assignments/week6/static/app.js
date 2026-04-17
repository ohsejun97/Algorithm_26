async function checkPlagiarism() {
    const textA = document.getElementById('textA').value;
    const textB = document.getElementById('textB').value;
    const checkBtn = document.getElementById('checkBtn');
    
    if (!textA || !textB) {
        alert("Please enter text in both fields.");
        return;
    }

    checkBtn.disabled = true;
    checkBtn.innerText = "Checking...";

    try {
        const response = await fetch('/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text_a: textA,
                text_b: textB
            })
        });

        const data = await response.json();

        // UI 업데이트
        document.getElementById('resultSection').classList.remove('hidden');
        document.getElementById('similarity').innerText = `${data.similarity}%`;
        document.getElementById('lcsLength').innerText = data.lcs_length;
        document.getElementById('lcsString').innerText = data.lcs_string || "(None)";

        const diffView = document.getElementById('diffView');
        diffView.innerHTML = '';
        
        data.diff.forEach(part => {
            const span = document.createElement('span');
            span.innerText = part.char;
            span.className = `diff-${part.type}`;
            diffView.appendChild(span);
        });

        // 결과 영역으로 스크롤
        document.getElementById('resultSection').scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while checking plagiarism.");
    } finally {
        checkBtn.disabled = false;
        checkBtn.innerText = "Check Similarity";
    }
}
