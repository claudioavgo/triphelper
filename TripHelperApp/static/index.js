const select = document.querySelector("#countrySelect");

select.addEventListener("change", (e) => {
    console.log(e.target.value)
})

function findCities(country) {
    fetch(`api/${country}/cities`).then(text => console.log(text))
}