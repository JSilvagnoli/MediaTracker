export async function getData(){
    const params = new URLSearchParams(window.location.search);
    const type = params.get("type");

    const response = await fetch(
        "http://127.0.0.1:8000/media?media_type="
        + encodeURIComponent(type)
    );

    if (response.status === 200){
        return await response.json();
    }
}

document.querySelector(".sort").addEventListener("change", async () => {
    const data = document.getElementById("results");
    const sortType = document.querySelector(".sort").value;

    const media = await getData();

    sortBy(media, sortType);
});

export async function displayData(data){
    const container = document.getElementById("results");

    data.forEach(media => {
        const card = document.createElement("div");

        const cardData = {
            id: media.id,
            title: media.title,
            description: media.description,
            releaseDate: media.release_date,
            rating: media.rating,
            image: media.image,
            type: media.type
        };
        
        Object.entries(cardData).forEach(([key, value]) => {
            card.dataset[key] = value;
        });

        const favoriteIcon = media.favorite_status ? "★" : "☆";
        const cardImg = media.image || "./No_Image_Available.jpg";
        const userRating = media.personal_rating || 0;

        card.innerHTML = `
            <button type="button" class="favoriteBtn">${favoriteIcon}</button>
            <button type="button" class="deleteBtn">X</button>
            <h1>${media.title}</h1>
            <img src="${cardImg}">
            <h2>Release Date: ${media.release_date}</h2>
            <p>${media.description}</p>
            <h2>Rating: ${media.rating}</h2>
            <label for="rating">Your Rating (0-10):</label>
            <input class="personalRating" type="number" id="rating" name="rating" min="0" max="10" value="${userRating}" step="1">
            <label for="completionStatus">Completion Status:</label>
            <select class="completionStatus" name="completionStatus">
                <option value="not started">Not Started</option>
                <option value="in progress">In Progress</option>
                <option value="completed">Completed</option>
            </select>
        `;

        const favoriteButton = card.querySelector(".favoriteBtn");

        favoriteButton.addEventListener("click", () => {
            if (favoriteButton.textContent === "☆") {
                favoriteButton.textContent = "★";
                media.favorite_status = true;
            }
            else {
                favoriteButton.textContent = "☆";
                media.favorite_status = false;
            }

            updateFavoriteStatus(media);
        });

        const deleteButton = card.querySelector(".deleteBtn");

        deleteButton.addEventListener("click", () => {
            deleteMedia(media);
        });

        const completionStatus = card.querySelector(".completionStatus");
        completionStatus.value = media.completion_status;

        completionStatus.addEventListener("change", function(event) {
            media.completion_status = completionStatus.value;

            updateCompletionStatus(media);
        });

        const rating = card.querySelector(".personalRating");

        rating.addEventListener("change", function(event) {
            media.personal_rating = rating.value;

            updatePersonalRating(media);
        });

        container.appendChild(card);
    });     
}

async function updateFavoriteStatus(media){
    const response = await fetch(
        "http://127.0.0.1:8000/updateFavoriteStatus", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

async function deleteMedia(media){
    const response = await fetch(
        "http://127.0.0.1:8000/deleteMedia", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

async function updateCompletionStatus(media){
    const response = await fetch(
        "http://127.0.0.1:8000/updateCompletionStatus", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

async function updatePersonalRating(media){
    const response = await fetch(
        "http://127.0.0.1:8000/updatePersonalRating", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

export async function sortBy(media, sortType){
    if (sortType === "alphabetical"){
        media.sort((a, b) => a.title.localeCompare(b.title));
    }
    else if (sortType === "date added"){
        media.sort((a, b) => b.date_added.localeCompare(a.date_added));
    }
    else if (sortType === "favorite"){
        media.sort((a, b) => b.favorite_status - a.favorite_status);
    }
    else if (sortType === "completion status"){
        media.sort((a, b) => a.completion_status.localeCompare(b.completion_status));
    }
    else if (sortType === "personal rating"){
        media.sort((a, b) => b.personal_rating - a.personal_rating);
    }
    else if (sortType === "user rating"){
        media.sort((a, b) => b.rating - a.rating);
    }

    const container = document.getElementById("results");
    container.replaceChildren();

    displayData(media);
}