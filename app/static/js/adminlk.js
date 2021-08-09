function openCloseDayCard(event) {
   event.target.classList.toggle('open')
}
function main() {
   $('.day').click(openCloseDayCard)
}

document.addEventListener('DOMContentLoaded', main)