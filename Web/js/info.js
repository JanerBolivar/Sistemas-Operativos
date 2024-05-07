document.addEventListener("DOMContentLoaded", () => {
  fetch("../data/tourist-sites.json")
    .then((response) => response.json())
    .then((data) => {
      // Filtrar el sitio basado en el valor de 'status'
      const filteredSites = data.sites.filter(site => site.label === data.status);
      const site = filteredSites[0];

      // Actualizar el src del video
      const videoElement = document.getElementById("myVideo");
      videoElement.src = site.video;

      // Actualizar el src de la imagen
      const imageElement = document.getElementById("siteImage");
      imageElement.src = site.img;

      // Actualizar el nombre del sitio
      const siteNameElement = document.getElementById("siteName");
      siteNameElement.textContent = site.nameSite;

      // Actualizar la ubicación del sitio
      const siteLocationElement = document.getElementById("siteLocation");
      siteLocationElement.textContent = `${site.country}, ${site.city}`;

      // Actualizar el contenido del div con el summary del sitio
      const summaryElement = document.getElementById('siteSummary');
      summaryElement.innerHTML = site.summary;

      // Actualizar las coordenadas del mapa
      const latitud = site.location.latitud;
      const longitud = site.location.longitud;
      const map = L.map("leafletmap").setView([latitud, longitud], 13);

      // Definir el layer de calles de Mapbox
      const streets = L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox/streets-v11",
          tileSize: 512,
          zoomOffset: -1,
          accessToken:
            "pk.eyJ1IjoidG9xdWlub3ZpYyIsImEiOiJjbGdiZ3VhZmMwaGdnM2Vud2Z2aWJjbnBiIn0.0D301Nbyl2uxrRs5Iic0mA",
        }
      );

      // Añadir el layer de calles al mapa
      streets.addTo(map);

      // Añadir un marcador al mapa
      L.marker([latitud, longitud]).addTo(map);
    })
    .catch((error) => console.error("Error al cargar el archivo JSON:", error));
});
