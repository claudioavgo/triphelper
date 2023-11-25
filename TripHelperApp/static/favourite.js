async function dislike(iso2, country, city, reload) {
    const data = await fetch(
        `/api/feed?country=${country}&city=${city}&type=dislike&iso2=${iso2}`
    );
    const data_returned = data.json();

    console.log(data_returned);
    
    if (reload)
        location.reload();
}

async function like(iso2, country, city) {
    const data = await fetch(
        `/api/feed?country=${country}&city=${city}&type=Like&iso2=${iso2}`
    );
    const data_returned = data.json();

    console.log(data_returned);
}

try {
    const like_element = document.getElementById("like");
    const heart = document.querySelector('#likeFav');
    if (heart.getAttribute('fill') == "gray") {
        like_element.addEventListener("click", (e) => {
            const iso2 = window.location.href.split("/")[4];
            const city = window.location.href.split("/")[5];
            const country = document.querySelector("#country").innerText;
            like(iso2, country, city);
            heart.setAttribute("fill", "red");
        });
    } else {
        like_element.addEventListener("click", (e) => {
            const iso2 = window.location.href.split("/")[4];
            const city = window.location.href.split("/")[5];
            const country = document.querySelector("#country").innerText;
            dislike(iso2, country, city, false);
            heart.setAttribute("fill", "gray");
        });
    }
} catch (e) {
    console.log();
}

try {
    const dislike_element = document.querySelectorAll(".dislike");

    dislike_element.forEach(element => {
        element.addEventListener("click", (e) => {
            dislike(element.attributes[0].value, element.attributes[1].value, element.attributes[2].value, true);
        });
    });
} catch (e) {
    console.log(e);
}



