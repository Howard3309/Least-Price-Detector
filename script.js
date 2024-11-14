async function findPrices() {
    const productName = document.getElementById('productName').value;

    if (!productName) {
        alert('Please enter a product name.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/get-prices', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ product_name: productName })
        });

        const result = await response.json();
        displayResult(result);
    } catch (error) {
        console.error('Error fetching prices:', error);
    }
}

function displayResult(data) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    if (data.error) {
        resultDiv.innerHTML = `<p>${data.error}</p>`;
    } else {
        const item = data.best_price;
        resultDiv.innerHTML = `
            <h3>Best Price Found</h3>
            <p>Site: ${item.site}</p>
            <p>Product: ${item.title}</p>
            <p>Price: ₹${item.price}</p>
        `;
    }
}
