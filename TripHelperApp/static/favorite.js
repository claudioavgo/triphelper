async function dislike(br, country, city) {
    const data = await fetch(
        "/api/feed?country=Brazil&city=Recife&type=Like&iso2=BR"
    );
    return data.json();
}

async function like(br, country, city) {
    const data = await fetch(
        "/api/feed?country=Brazil&city=Recife&type=like&iso2=BR"
    );
    return data.json();
}