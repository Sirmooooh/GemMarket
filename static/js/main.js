document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript loaded!');

    // Example function to handle a button click
    function handleButtonClick() {
        alert('Button clicked!');
    }

    // Example function to toggle visibility of an element
    function toggleVisibility() {
        const element = document.getElementById('toggleElement');
        if (element) {
            element.style.display = (element.style.display === 'none') ? 'block' : 'none';
        }
    }

    // Example function to fetch data from an API
    async function fetchData() {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
            const data = await response.json();
            console.log('Fetched data:', data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Attach event listeners to elements
    const button = document.getElementById('myButton');
    const toggleButton = document.getElementById('toggleButton');
    const fetchDataButton = document.getElementById('fetchDataButton');

    if (button) {
        button.addEventListener('click', handleButtonClick);
    }

    if (toggleButton) {
        toggleButton.addEventListener('click', toggleVisibility);
    }

    if (fetchDataButton) {
        fetchDataButton.addEventListener('click', fetchData);
    }
});
