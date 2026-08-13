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

    const resultsElement = document.getElementById("results");

    for (const media of data){
        console.log(media);

        const card = document.createElement("div");

        const title = document.createElement("h1");
        const image = document.createElement("img");
        const release_date = document.createElement("h2");
        const description = document.createElement("h2");
        const rating = document.createElement("h2");
        const id = document.createElement("h2");

        title.textContent = media.title;
        image.src = media.image;
        release_date.textContent = "Release Date: " + media.release_date;
        description.textContent = media.description;
        rating.textContent = "Rating: " + media.rating;
        id.textContent = "ID: " + media.id;

        card.appendChild(title);
        card.appendChild(image);
        card.appendChild(release_date);
        card.appendChild(description);
        card.appendChild(rating);
        card.appendChild(id);

        resultsElement.appendChild(card);
    }
}