document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('searchInput').value.trim();
    if (input) {
        displaySection('search');
        displayRecipes(input);
    } else {
        document.getElementById('recipesContainer').innerHTML = '<p>Please enter a search term.</p>';
    }
});

function displaySection(sectionId) {
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        if (section.id === sectionId) {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });
}

document.getElementById('homeLink').addEventListener('click', function(event) {
    event.preventDefault();
    displaySection('home');
});

document.getElementById('recipesLink').addEventListener('click', function(event) {
    event.preventDefault();
    displaySection('search');
});

document.getElementById('aboutLink').addEventListener('click', function(event) {
    event.preventDefault();
    displaySection('about');
});

function displayRecipes(searchQuery) {
    // Fetch recipes from the backend API
    fetch(`http://localhost:5000/api/recipes?search=${encodeURIComponent(searchQuery)}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');  // Handle non-200 responses
        }
        return response.json();
    })
    .then(recipes => {
        let recipesContainer = document.getElementById('recipesContainer');
        recipesContainer.innerHTML = ''; // Clear previous results

        if (recipes.length === 0) {
            recipesContainer.innerHTML = '<p>No recipes found. Try a different search!</p>';  // Display a message if no recipes are found
        } else {
            recipes.forEach(recipe => {
                let elem = document.createElement('div');
                elem.classList.add('recipe');  // Add a class for styling
                elem.innerHTML = `<h3>${recipe.recipeName}</h3>
                                  <p>${recipe.description || 'No description available'}</p>
                                  <p>Calories: ${recipe.totalCalories.toFixed(2)} kcal</p>
                                  <p>Protein: ${recipe.protein.toFixed(2)} g, Carbs: ${recipe.carbs.toFixed(2)} g, Fat: ${recipe.fat.toFixed(2)} g</p>
                                  <p>Health Index: ${recipe.healthIndex.toFixed(2)}</p>`;
                recipesContainer.appendChild(elem);
            });
        }
    })
    .catch(error => {
        console.error('Error fetching recipes:', error);
        document.getElementById('recipesContainer').innerHTML = '<p style="color: red;">Failed to load recipes. Please check your connection and try again.</p>';
    });
}
