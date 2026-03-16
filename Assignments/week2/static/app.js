document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchIdBtn = document.getElementById('searchIdBtn');
    const searchNameBtn = document.getElementById('searchNameBtn');
    const findDuplicatesBtn = document.getElementById('findDuplicatesBtn');
    const resultsContainer = document.getElementById('resultsContainer');
    const statusInfo = document.getElementById('statusInfo');
    const complexityBadge = document.getElementById('complexityBadge');
    const executionTime = document.getElementById('executionTime');

    const updateStatus = (complexity, time) => {
        statusInfo.classList.remove('hidden');
        complexityBadge.textContent = complexity;
        executionTime.textContent = `Execution Time: ${time.toFixed(4)} ms`;
        
        // 색상 변경
        if (complexity === 'O(1)') complexityBadge.style.backgroundColor = '#4a90e2';
        else if (complexity === 'O(n)') complexityBadge.style.backgroundColor = '#f39c12';
        else if (complexity === 'O(n²)') complexityBadge.style.backgroundColor = '#e74c3c';
    };

    const renderProducts = (products) => {
        resultsContainer.innerHTML = '';
        if (products.length === 0) {
            resultsContainer.innerHTML = '<div class="placeholder">No products found.</div>';
            return;
        }
        products.forEach(p => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <div class="id">ID: ${p.id}</div>
                <h3>${p.name}</h3>
                <div class="category">${p.category}</div>
                <div class="price">$${p.price}</div>
            `;
            resultsContainer.appendChild(card);
        });
    };

    const renderDuplicates = (duplicates) => {
        resultsContainer.innerHTML = '';
        if (duplicates.length === 0) {
            resultsContainer.innerHTML = '<div class="placeholder">No duplicates found.</div>';
            return;
        }
        duplicates.forEach(d => {
            const div = document.createElement('div');
            div.className = 'duplicate-card';
            div.innerHTML = `
                <span><strong>${d.item1.name}</strong> (ID: ${d.item1.id} & ${d.item2.id})</span>
                <span class="category">${d.item1.category}</span>
            `;
            resultsContainer.appendChild(div);
        });
    };

    searchIdBtn.addEventListener('click', async () => {
        const id = searchInput.value.trim();
        if (!id) return alert('Please enter an ID');
        const resp = await fetch(`/search/id?id=${id}`);
        const data = await resp.json();
        updateStatus(data.complexity, data.execution_time_ms);
        renderProducts(data.results);
    });

    searchNameBtn.addEventListener('click', async () => {
        const q = searchInput.value.trim();
        const resp = await fetch(`/search/name?q=${q}`);
        const data = await resp.json();
        updateStatus(data.complexity, data.execution_time_ms);
        renderProducts(data.results);
    });

    findDuplicatesBtn.addEventListener('click', async () => {
        resultsContainer.innerHTML = '<div class="placeholder">Processing O(n²)... Please wait.</div>';
        const resp = await fetch('/search/duplicates');
        const data = await resp.json();
        updateStatus(data.complexity, data.execution_time_ms);
        renderDuplicates(data.results_sample);
    });
});
