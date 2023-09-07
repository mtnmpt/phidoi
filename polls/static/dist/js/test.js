// script.js
// tạo ra 3 biến để: mở popup, đóng popup, lấy popup
const openPopupButton = document.getElementById('openPopup'); // mở popup
const closePopupButton = document.getElementById('closePopup');// đóng popup
const popup = document.getElementById('popup'); //lấy popup

//sự kiện click thì hiển thị popup
openPopupButton.addEventListener('click', () => {
    popup.style.display = 'flex';
});

// sự kiện click thì đóng popup
closePopupButton.addEventListener('click', () => {
    popup.style.display = 'none';
});
