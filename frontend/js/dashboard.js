document.addEventListener('DOMContentLoaded', () => {
    // Security Check: Redirect if not admin
    const userJson = localStorage.getItem('user');
    if (!userJson) {
        window.location.href = 'login.html';
        return;
    }

    const user = JSON.parse(userJson);
    if (!user.is_admin) {
        alert('Access denied: Admins only.');
        window.location.href = 'index.html';
        return;
    }

    // Fetch and populate stats
    fetchStats(user.email);
});

async function fetchStats(email) {
    try {
        const response = await fetch(`http://localhost:8000/api/admin/stats?email=${encodeURIComponent(email)}`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch stats');
        }

        const data = await response.json();
        
        // Update Total Users
        document.getElementById('totalUsers').textContent = data.total_users;

        // Update Breakdown
        populateBreakdown(data.prediction_breakdown);

        // Update Recent Predictions
        populateRecentPredictions(data.recent_predictions);

    } catch (error) {
        console.error('Error loading dashboard:', error);
        document.querySelectorAll('.loading-text').forEach(el => {
            el.textContent = 'Error loading data. Check console.';
        });
    }
}

function populateBreakdown(breakdown) {
    const list = document.getElementById('breakdownList');
    list.innerHTML = '';

    const types = Object.keys(breakdown);
    if (types.length === 0) {
        list.innerHTML = '<p class="loading-text">No predictions logged yet.</p>';
        return;
    }

    types.forEach(type => {
        const item = document.createElement('div');
        item.className = 'breakdown-item';
        item.innerHTML = `
            <span class="breakdown-label">${capitalize(type)}</span>
            <span class="breakdown-count">${breakdown[type]}</span>
        `;
        list.appendChild(item);
    });
}

function populateRecentPredictions(predictions) {
    const body = document.getElementById('recentPredictionsBody');
    body.innerHTML = '';

    if (predictions.length === 0) {
        body.innerHTML = '<tr><td colspan="4" class="loading-text">No recent activity.</td></tr>';
        return;
    }

    predictions.forEach(p => {
        const row = document.createElement('tr');
        const date = new Date(p.timestamp).toLocaleString();
        
        row.innerHTML = `
            <td>${p.fullname}</td>
            <td><span class="breakdown-count" style="background: rgba(255,255,255,0.1);">${capitalize(p.type)}</span></td>
            <td>${p.outcome}</td>
            <td style="color: var(--text-muted); font-size: 0.8rem;">${date}</td>
        `;
        body.appendChild(row);
    });
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
