$('.header-burger-menu').on('click', (e) => {
  toggleMHeader();
});

$('.search_open').on('click', (e) => {
  openSearch();
})

$('.search_close').on('click', (e) => {
  closeSearch();
})

$('.image-viewer-close').on('click', (e) => {
  closeImageViewer();
})

let imageViewer = document.querySelector('.image-viewer');
let imageViewerTitleSlot = imageViewer.querySelector('.image-viewer-title')
let imageViewerImgSlot = imageViewer.querySelector('img')

document.addEventListener('keydown', (event) => {
  if (event.code === 'Escape') {
    closeAllFixed()
  }
})

let filesElements = document.querySelectorAll('.fond-folder.file');
for (let i = 0; i < filesElements.length; i++) {
  filesElements[i].addEventListener('click', (event) => {
    let element = filesElements[i]
    openImageViewer(element.querySelector('img').src, title = element.querySelector('.fond-folder-info-title').innerHTML)
  })
}

function toggleMHeader() {
  closeAllFixed()
  $('.header-nav').toggleClass('active');
}

function openImageViewer(src, title = 'Просмотр документа',) {
  closeAllFixed()
  imageViewerTitleSlot.innerHTML = title
  imageViewerImgSlot.src = src;
  imageViewer.classList.remove('hide')
}

function openSearch() {
  closeAllFixed()
  $('.search_wrapper').addClass('showed')
}

function openMHeader() {
  closeAllFixed()
  $('.header-nav').addClass('active');
}

function closeImageViewer() {
  imageViewer.classList.add('hide')
  imageViewerTitleSlot.innerHTML = 'title'
  imageViewerImgSlot.src = ''
}

function closeSearch() {
  $('.search_wrapper').removeClass('showed')
}

function closeMHeader() {
  $('.header-nav').removeClass('active');
}

function closeAllFixed() {
  closeSearch()
  closeImageViewer()
  closeMHeader()
}