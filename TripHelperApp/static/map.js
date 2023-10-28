var map = new Datamap({ element: document.getElementById("container") });

const country_input = document.getElementById("countrySelect");

map.svg.selectAll(".datamaps-subunit").on("click", async function (geography) {
  const iso2 = await iso3toiso2(geography.id);
  console.log(iso2);
  setCountry(iso2);
});

function setCountry(country) {
  country_input.value = country;
  country_input.subumit();
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
