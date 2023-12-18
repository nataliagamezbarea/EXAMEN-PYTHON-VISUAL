function calculateIMC() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const system = document.querySelector('input[name="system"]:checked');

    if (weight > 0 && height > 0 && system) {
        let heightInMeters = height; // Default assumption: Metric system

        if (system.value === 'english') {
            heightInMeters *= 0.0254; // Convert height to meters if using the English system
        } else {
            heightInMeters /= 100; // Convert height from cm to meters (already in meters for metric)
        }

        const imc = weight / (heightInMeters * heightInMeters);

        let message = `Tu IMC es: ${imc.toFixed(2)}. `;
        let category = '';

        if (imc < 18.5) {
            category = 'Peso inferior al normal';
        } else if (imc < 25) {
            category = 'Normal';
        } else if (imc < 30) {
            category = 'Peso superior al normal';
        } else {
            category = 'Obesidad';
        }

        message += `Categoría: ${category}`;
        document.getElementById('result').innerText = message;
    } else {
        alert('Por favor, ingresa valores válidos para peso y altura.');
    }
}
