function onKonamiCode() {
    window.location.href = './theme/egg/game.html'
}
function onKonamiCodeGesture(event) {
  console.log(event.detail.name);
}
document.addEventListener("konamiCode", onKonamiCode);
document.addEventListener("konamiCodeGesture", onKonamiCodeGesture);