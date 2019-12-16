$(function () {
    initTopSwiper();
    initSwipMenu();
})

function initTopSwiper() {
    var swiper = new Swiper("#topSwiper",{
        loop: true,
        autoplay: 3000,
        pagination: '.swiper-pagination'
    })
}

function initSwipMenu() {
    var swiper = new Swiper("#swiperMenu",{
       slidesPerView: 3,
    })
}