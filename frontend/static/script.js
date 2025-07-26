document.getElementById('prediction-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const resultDiv = document.getElementById('result');
  resultDiv.style.display = 'none';

  // Show loading state
  const submitBtn = e.target.querySelector('button');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Predicting...';
  submitBtn.disabled = true;

  try {
    const data = {
      qual: parseInt(document.getElementById('qual').value),
      area: parseFloat(document.getElementById('area').value),
      beds: parseInt(document.getElementById('beds').value),
      baths: parseFloat(document.getElementById('baths').value),
      year: parseInt(document.getElementById('year').value),
      garage: parseInt(document.getElementById('garage').value),       // New field
      neighborhood: parseInt(document.getElementById('neighborhood').value) // New field
    };

    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    
    if (result.error) {
      resultDiv.className = 'alert alert-danger';
      resultDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> Error: ${result.error}`;
    } else {
      resultDiv.className = 'alert alert-success';
      resultDiv.innerHTML = `
        <i class="fas fa-check-circle"></i> Predicted Price: 
        <strong>$${result.price.toLocaleString()}</strong>
      `;
    }
  } catch (error) {
    resultDiv.className = 'alert alert-danger';
    resultDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> Network Error: ${error.message}`;
  } finally {
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;
    resultDiv.style.display = 'block';
  }
});