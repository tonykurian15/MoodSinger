var loader = document.querySelector(".mega-container");
var displayBox = document.querySelector(".display-box");
var mood = document.getElementById("mood");
var playlistLink = document.getElementById("playlist-link");
var playlist = document.getElementById("playlist");
// setTimeout(()=>{
//   location.reload(20000);
// },)

fetch('/api/geo_code')
  .then((response) => (response.json()))
  .then((data) => {
    console.log(data)  
    if (data.mood != "") {
      loader.style.display = "none";
      displayBox.style.opacity = 1;
      mood.innerHTML = `You are feeling `+data.mood+` now`;
      playlist.addEventListener('click', ()=>{
          playlistLink.setAttribute("href",data.play);
      }) 
    }
  })
  //.catch((err) => console.log("Error"));

