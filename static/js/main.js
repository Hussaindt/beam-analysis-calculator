document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Get form values
    const concrete_mix = document.getElementById('concrete_mix').value;
    const breadth = document.getElementById('breadth').value;
    const depth = document.getElementById('depth').value;
    const length = document.getElementById('length').value;
    
    try {
        // Show loading state
        const button = this.querySelector('button[type="submit"]');
        const originalText = button.innerHTML;
        button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Calculating...';
        button.disabled = true;
        
        // Make API call
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                concrete_mix: concrete_mix,
                breadth: breadth,
                depth: depth,
                length: length
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Update only elastic modulus result
            document.getElementById('elastic-modulus-result').textContent = 
                `${data.elastic_modulus} N/mm²`;
            
            // Show results section
            document.getElementById('results').style.display = 'block';
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        // Restore button state
        button.innerHTML = originalText;
        button.disabled = false;
    }
}); 