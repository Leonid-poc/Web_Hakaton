$('.header-burger-menu').on('click', (e) => {
  $('.header-nav').toggleClass('active');
});

let q = document.getElementsByClassName('news-post-desc')
for (i of q) {
    i.innerHTML = i.innerHTML.slice(0, 364) + '...'
}
