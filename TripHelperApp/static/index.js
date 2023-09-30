const select = document.querySelector("#countrySelect");
const selectCity = document.querySelector("#countrySelectCity")

// async function fetchCitiesData(country) {
//     try {
//       const response = await fetch(`api/${country}/cities`);
      
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
      
//       const data = await response.json();
//       return data;
//     } catch (error) {
//       throw error;
//     }
//   }

// select.addEventListener("change", (e) => {
//     console.log(fetchCitiesData(e.target.value))
//     selectCity.style.display = "block"
// })