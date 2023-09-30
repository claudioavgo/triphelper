const select = document.querySelector("#countrySelect");
const selectCity = document.querySelector("#countrySelectCity")

async function fetchCitiesData(country) {
    try {
      const response = await fetch(`api/${country}/cities`);
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      const data = await response.json();
      return data;
    } catch (error) {
      throw error;
    }
  }

select.addEventListener("change", async (e) => {

    selectCity.style.display = "none"

    removeOptions(selectCity);

    const cities_list = await fetchCitiesData(e.target.value)
    
    var option = document.createElement("option");
    option.text = "Choose your city";
    option.selected = true;
    selectCity.add(option);

    for (const item of cities_list.cities) {
        var option = document.createElement("option");
        option.text = item;
        selectCity.add(option);
    }

    selectCity.style.display = "block"
})

function removeOptions(selectElement) {
    var i, L = selectElement.options.length - 1;
    for(i = L; i >= 0; i--) {
       selectElement.remove(i);
    }
 }