const select = document.querySelector("#countrySelect");
const selectCity = document.querySelector("#countrySelectCity");
const loader1 = document.querySelector("#loader1");
const conSelectCity = document.querySelector("#containerSelectCity");
const attBtn = document.querySelector("#attBtn")

async function fetchCitiesData(country) {
  try {
    const response = await fetch(`api/${country}/cities`);

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    throw error;
  }
}

select.addEventListener("change", async (e) => {
  if (e.target.value.includes("Choose")) {conSelectCity.style.display = "none";loader1.style.display = "none";}
  else {
    conSelectCity.style.display = "none";
    loader1.style.display = "flex";
  
    removeOptions(selectCity);
  
    const cities_list = await fetchCitiesData(e.target.value);
  
    var option = document.createElement("option");
    option.text = "Choose your city";
    option.selected = true;
    selectCity.add(option);
  
    for (const item of cities_list.cities) {
      var option = document.createElement("option");
      option.text = item;
      selectCity.add(option);
    }
  
    loader1.style.display = "none";
    conSelectCity.style.display = "flex";
  }
});

selectCity.addEventListener("change", (e)=> {
  if (e.target.value.includes("Choose")) {
    attBtn.style.display = "none"
  } else {
    attBtn.style.display = "block"
  }
})

attBtn.addEventListener("click", ()=> {
  attBtn.style.display = "none";
  loader1.style.display = "flex";
  window.location.href = `destination/${select.value}/${selectCity.value}`;
})

function removeOptions(selectElement) {
  var i,
    L = selectElement.options.length - 1;
  for (i = L; i >= 0; i--) {
    selectElement.remove(i);
  }
}