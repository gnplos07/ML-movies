const form = document.getElementById("movie-search");
const titleInput = document.getElementById("movie-title");
const searchStatus = document.getElementById("search-status");
const results = document.getElementById("recommendations");
const submitButton = form.querySelector('button[type="submit"]');

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (submitButton.disabled) {
        return;
    }

    results.replaceChildren();
    const title = titleInput.value.trim();
    if (!title) {
        searchStatus.textContent = "Enter a movie title.";
        return;
    }

    submitButton.disabled = true;
    searchStatus.textContent = "Finding similar movies…";

    try {
        const response = await fetch(`/recommend?title=${encodeURIComponent(title)}`);
        if (response.status === 404) {
            searchStatus.textContent = "Movie not found.";
            return;
        }
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        const movies = await response.json();
        for (const movie of movies) {
            const item = document.createElement("li");
            item.textContent = `${movie.title} (${movie.score.toFixed(3)})`;
            results.appendChild(item);
        }
        searchStatus.textContent = "";
    } catch {
        searchStatus.textContent = "Could not load recommendations. Try again.";
    } finally {
        submitButton.disabled = false;
    }
});
