document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    getInput();
});

document.getElementById("type").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        getInput();
    }
});

async function getInput(){
    var input = document.getElementById("input");
    var dropdown = document.getElementById("type");

    const media_to_find = input.value;
    const media_type = dropdown.value;

    const response = await fetch(
        "http://127.0.0.1:8000/search?media_to_find=" 
        + encodeURIComponent(media_to_find) 
        + "&media_type="
        + encodeURIComponent(media_type)
    );

    const data = await response.json();

    const container = document.getElementById("results");

    data.forEach(media => {
        const card = document.createElement("div");

        card.dataset.id = media.id;
        card.dataset.title = media.title;
        card.dataset.image = media.image;
        card.dataset.releaseDate = media.release_date;
        card.dataset.description = media.description;
        card.dataset.rating = media.rating;
        card.dataset.mediaType = media_type;

        card.innerHTML = `
            <h1>${media.title}</h2>
            <img src=${media.image}>
            <h2>Release Date: ${media.release_date}</h2>
            <p>${media.description}</p>
            <h2>Rating: ${media.rating}</h2>
        `;

        card.addEventListener("click", () => {
            // Instead of printing to the console, ask the user if they want to save this movie to their list, and send it back to python then to sqlite3
            console.log(
                card.dataset.id 
                + " " + card.dataset.title 
                + " " + card.dataset.description
                + " " + card.dataset.releaseDate 
                + " " + card.dataset.rating 
                + " " + card.dataset.image 
                + " " + card.dataset.mediaType
            );
        });

        container.appendChild(card);
    });
        
}