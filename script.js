document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('searchInput').value;
    displayRecipes(input);
});

function displayRecipes(searchQuery) {
    // This should be replaced with an API call to your backend
    let mockRecipes = [
        { name: "Avocado Salad", description: "A fresh salad with avocados, cherry tomatoes, and pine nuts." },
        { name: "Quinoa Pilaf", description: "Delicious quinoa with mixed vegetables, cooked to perfection." }
    ];

    let recipesContainer = document.getElementById('recipesContainer');
    recipesContainer.innerHTML = ''; // Clear previous results

    mockRecipes.forEach(recipe => {
        if(recipe.name.toLowerCase().includes(searchQuery.toLowerCase())) {
            let elem = document.createElement('div');
            elem.innerHTML = `<h3>${recipe.name}</h3><p>${recipe.description}</p>`;
            recipesContainer.appendChild(elem);
        }
    });
}
