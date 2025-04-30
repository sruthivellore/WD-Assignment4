document.addEventListener('DOMContentLoaded', () => {
    const numberInput = document.getElementById('number-input');
    const fileInput = document.getElementById('file-upload');
    const cartCount = document.getElementById('cart-count');

    function updateCartCount(numbers) {
        const numberArray = numbers
            .split(',')
            .map(n => n.trim())
            .filter(n => n !== '' && !isNaN(n));

        const uniqueNumbers = [...new Set(numberArray)];
        cartCount.textContent = uniqueNumbers.length;
    }

    numberInput.addEventListener('input', () => {
        updateCartCount(numberInput.value);
    });

    fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const content = e.target.result;
                numberInput.value = content;
                updateCartCount(content);
            };
            reader.readAsText(file);
        }
    });
});