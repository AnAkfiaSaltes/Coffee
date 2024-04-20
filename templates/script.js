<script>
    function addItem(itemImage, itemPrice) {
        fetch('/select_item', {
            method: 'POST',
            body: JSON.stringify({
                item_index: 7,  // Произвольный индекс для обозначения добавления цены в папку
                item_price: itemPrice
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.text())
        .then(message => console.log(message))
        .catch(error => console.error('Error:', error));
    }

    function showSelectedItem() {
        fetch('/select_item', {
            method: 'POST',
            body: JSON.stringify({
                item_index: 7  // Индекс для отображения выбранного товара
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.text())
        .then(item => {
            // Здесь можно сделать что-то с выбранным товаром, например, отобразить его
            console.log('Selected Item:', item);
        })
        .catch(error => console.error('Error:', error));
    }
</script>