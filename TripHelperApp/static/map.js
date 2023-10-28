var map = new Datamap({ 
    element: document.getElementById("container"), 
    fills: {          
        'defaultFill': '#3D45FB',
    },
    geographyConfig: {
        "borderColor": '#212529',
        highlightFillColor: '#fa0fa0',
        borderWidth: 3,
        popupTemplate: function(geography, data) { //this function should just return a string
            return '<div><strong>' + geography.properties.name + '</strong></div>';
        },
    },
});

const country_input = document.getElementById("countrySelect");

map.svg.selectAll(".datamaps-subunit").on("click", async function (geography) {
  const iso2 = await iso3toiso2(geography.id);
  setCountry(iso2);
});

function setCountry(country) {
  country_input.value = country;
  country_input.dispatchEvent(new Event("change"))
}

async function getCountries() {
  const data = await fetch(
    "https://raw.githubusercontent.com/claudioavgo/triphelper/main/TripHelperApp/static/bin/countries.json"
  );
  return data.json();
}

async function iso3toiso2(iso3) {
  try {
    const data = await getCountries();

    for (let i of data["data"]) {
      if (i["iso3"] == iso3) {
        return i["iso2"];
      }
    }
  } catch (error) {
    console.log(error);
    return null;
  }
}
