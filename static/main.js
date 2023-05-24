// Dictionary with country names as keys

// fetch(url)
//   .then(response => response.json())
//   .then(data => {
//     // Populate the worldMapNames dictionary
//     data.forEach( item => {
//         var key = item.country_name;
//         var value = item.data_value;
//         worldMapNames[key] = value
//     })
//     // Access and work with the populated dictionary
//     console.log(worldMapNames);
//   })
//   .catch(error => {
//     console.error('Error:', error);
//   });
// console.log(`World: ${worldMapNames}`)

function fetchCountryData(worldMapNames) {
  
  const url = "/country_data_json/";
  return new Promise(async (resolve, reject) => {
    try {
      const response = await fetch(url);
      const data = await response.json();
      data.forEach((item) => {
        var key = item.country_name;
        var value = item.data_value;
        worldMapNames[key] = value;
        console.log(`${key}:${worldMapNames[key]}`);
      });
      resolve();
    } catch (error) {
      reject(error);
    }
  });
}

(async () => {
  try {
    var worldMapNames = {};
    await fetchCountryData(worldMapNames);
    
    const worldMapCodes = {
      AF: "Afghanistan",
      AX: "Aland Islands",
      AL: "Albania",
      DZ: "Algeria",
      AS: "American Samoa",
      AD: "Andorra",
      AO: "Angola",
      AI: "Anguilla",
      AQ: "Antarctica",
      AG: "Antigua and Barbuda",
      AR: "Argentina",
      AM: "Armenia",
      AW: "Aruba",
      AU: "Australia",
      AT: "Austria",
      AZ: "Azerbaijan",
      BS: "Bahamas",
      BH: "Bahrain",
      BD: "Bangladesh",
      BB: "Barbados",
      BY: "Belarus",
      BE: "Belgium",
      BZ: "Belize",
      BJ: "Benin",
      BM: "Bermuda",
      BT: "Bhutan",
      BO: "Bolivia",
      BQ: "Bonaire, Sint Eustatius and Saba",
      BA: "Bosnia and Herzegovina",
      BW: "Botswana",
      BV: "Bouvet Island",
      BR: "Brazil",
      IO: "British Indian Ocean Territory",
      BN: "Brunei Darussalam",
      BG: "Bulgaria",
      BF: "Burkina Faso",
      BI: "Burundi",
      KH: "Cambodia",
      CM: "Cameroon",
      CA: "Canada",
      CV: "Cape Verde",
      KY: "Cayman Islands",
      CF: "Central African Rep.",
      TD: "Chad",
      CL: "Chile",
      CN: "China",
      CX: "Christmas Island",
      CC: "Cocos (Keeling) Islands",
      CO: "Colombia",
      KM: "Comoros",
      CG: "Congo",
      CD: "Dem. Rep. Congo",
      CK: "Cook Islands",
      CR: "Costa Rica",
      CI: "C\u00f4te d'Ivoire",
      HR: "Croatia",
      CU: "Cuba",
      CW: "Curacao",
      CY: "Cyprus",
      XC: "N. Cyprus",
      CZ: "Czech Republic",
      DK: "Denmark",
      DJ: "Djibouti",
      DM: "Dominica",
      DO: "Dominican Republic",
      EC: "Ecuador",
      EG: "Egypt",
      GB: "United Kingdom",
      GQ: "Equatorial Guinea",
      ER: "Eritrea",
      EE: "Estonia",
      ET: "Ethiopia",
      FK: "Falkland Islands (Malvinas)",
      FO: "Faroe Islands",
      FJ: "Fiji",
      FI: "Finland",
      FR: "France",
      GF: "French Guiana",
      PF: "French Polynesia",
      TF: "Fr. S. Antarctic Lands",
      GA: "Gabon",
      GM: "Gambia",
      GE: "Georgia",
      DE: "Germany",
      GH: "Ghana",
      GI: "Gibraltar",
      GR: "Greece",
      GL: "Greenland",
      GD: "Grenada",
      GP: "Guadeloupe",
      GU: "Guam",
      GT: "Guatemala",
      GG: "Guernsey",
      GN: "Guinea",
      GW: "Guinea-Bissau",
      GY: "Guyana",
      HT: "Haiti",
      HM: "Heard Island and Mcdonald Islands",
      VA: "Holy See (Vatican City State)",
      HN: "Honduras",
      HK: "Hong Kong",
      HU: "Hungary",
      IS: "Iceland",
      IN: "India",
      ID: "Indonesia",
      IR: "Iran",
      IQ: "Iraq",
      IE: "Ireland",
      IM: "Isle of Man",
      IL: "Israel",
      IT: "Italy",
      JM: "Jamaica",
      JP: "Japan",
      JE: "Jersey",
      JO: "Jordan",
      KZ: "Kazakhstan",
      KE: "Kenya",
      KI: "Kiribati",
      KP: "Korea, Democratic People's Republic of",
      KR: "Korea, Republic of",
      KW: "Kuwait",
      KG: "Kyrgyzstan",
      XK: "Kosovo",
      LA: "Laos",
      LV: "Latvia",
      LB: "Lebanon",
      LS: "Lesotho",
      LR: "Liberia",
      LY: "Libya",
      LI: "Liechtenstein",
      LT: "Lithuania",
      LU: "Luxembourg",
      MK: "Macedonia",
      MG: "Madagascar",
      MW: "Malawi",
      MY: "Malaysia",
      MV: "Maldives",
      ML: "Mali",
      MT: "Malta",
      MH: "Marshall Islands",
      MQ: "Martinique",
      MR: "Mauritania",
      MU: "Mauritius",
      YT: "Mayotte",
      MX: "Mexico",
      FM: "Micronesia, Federated States of",
      MD: "Moldova, Republic of",
      MC: "Monaco",
      MN: "Mongolia",
      ME: "Montenegro",
      MS: "Montserrat",
      MA: "Morocco",
      MZ: "Mozambique",
      MM: "Myanmar",
      NA: "Namibia",
      NE: "Niger",
      NG: "Nigeria",
      NI: "Nicaragua",
      NL: "Netherlands",
      NO: "Norway",
      NP: "Nepal",
      NR: "Nauru",
      NU: "Niue",
      NZ: "New Zealand",
      OM: "Oman",
      PA: "Panama",
      PE: "Peru",
      PG: "Papua New Guinea",
      PH: "Philippines",
      PK: "Pakistan",
      PS: "Palestine",
      PL: "Poland",
      PT: "Portugal",
      PW: "Palau",
      PY: "Paraguay",
      QA: "Qatar",
      RO: "Romania",
      RS: "Serbia",
      RU: "Russia",
      RW: "Rwanda",
      SA: "Saudi Arabia",
      SB: "Solomon Islands",
      SC: "Seychelles",
      ES: "Spain",
      SD: "Sudan",
      SE: "Sweden",
      CH: "Switzerland",
      SG: "Singapore",
      SI: "Slovenia",
      SK: "Slovakia",
      SL: "Sierra Leone",
      SM: "San Marino",
      SN: "Senegal",
      SO: "Somalia",
      XS: "Somaliland",
      SR: "Suriname",
      SS: "South Sudan",
      ST: "Sao Tome and Principe",
      SV: "El Salvador",
      SY: "Syria",
      SZ: "Swaziland",
      LK: "Sri Lanka",
      TD: "Chad",
      TG: "Togo",
      TH: "Thailand",
      TJ: "Tajikistan",
      TL: "East Timor",
      TM: "Turkmenistan",
      TN: "Tunisia",
      TO: "Tonga",
      TR: "Turkey",
      TT: "Trinidad and Tobago",
      TV: "Tuvalu",
      TW: "Taiwan",
      TZ: "Tanzania",
      UA: "Ukraine",
      UG: "Uganda",
      US: "United States",
      AE: "United Arab Emirates",
      UY: "Uruguay",
      UZ: "Uzbekistan",
      VA: "Vatican City",
      VC: "Saint Vincent and the Grenadines",
      VE: "Venezuela",
      VN: "Vietnam",
      VU: "Vanuatu",
      EH: "W. Sahara",
      WS: "Samoa",
      YE: "Yemen",
      ZA: "South Africa",
      ZM: "Zambia",
      ZW: "Zimbabwe",
    };

    console.log(`map codes: ${worldMapCodes}`);
    function assignValues(countryValues, countryCodes) {
      let result = {};
      for (let code in countryCodes) {
        let name = countryCodes[code];
        if (name in countryValues) {
          result[code] = countryValues[name];
        }
      }
      return result;
    }

    var heatmapvals = assignValues(worldMapNames, worldMapCodes);

    $(function () {
      // Initialize the map
      $("#world-map").vectorMap({
        map: "world_mill",
        borderColor: "#000000",
        backgroundColor: "#ffffff",
        regionStyle: {
          initial: {
            fill: "#c3c1c1",
          },
        },
        onRegionTipShow: (e, el, c) => {
          el.html(
            `${worldMapCodes[c]}: ${worldMapNames[worldMapCodes[c]]} institutions`
          );
        },
        series: {
          regions: [
            {
              values: heatmapvals,
              legend: {
                vertical: false,
                title: "Coverage of Migration and Health Degrees",
              },
              scale: ["#b3e5fc", "#0d47a1"],
              normalizeFunction: "polynomial",
            },
          ],
        },
        legend: {
          vertical: true,
          title: "Heatmap Legend",
          labelRender: function (value) {
            return value.toFixed(2); // format legend labels to 2 decimal places
          },
        },
      });
    });

    console.log("end of script");

  } catch (error) {
    console.log(`An error occurred: ${error}`);
  }
})();
