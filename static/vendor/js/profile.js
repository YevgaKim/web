//Переключение между прокрутками аниме
// const checkbox = document.querySelector('input[type="checkbox"]'),
//       prok1 = document.querySelector(".prokrutka"),
//       prok2 = document.querySelector(".prokrutka2"),
//       but = document.querySelector(".but");   



// checkbox.addEventListener('change', function() {
//   if (this.checked) {
//     prok1.style.display = "none";
//     prok2.style.display = "block";
//     but.style.display = "none";
//   } else {
//     prok2.style.display = "none";
//     prok1.style.display = "block"
//     but.style.display = "block";
//   }
// });
//Кнопка добавления фото
const img = document.querySelector(".div_image"),
      img_photo = document.querySelector(".image_user"),
      plus = document.querySelector(".plus");

img.addEventListener("mouseover", event=>{
    img_photo.style.filter = "blur(5px)";
    plus.style.display = "block";
});
  
img.addEventListener("mouseout", event=>{
    img_photo.style.filter = "blur(0px)";
    plus.style.display = "none";
});

//Modal
const b = document.querySelector(".plus"),
      closeM = document.querySelector(".closeModal"),
      modal = document.querySelector(".modal");

function closeModal(){
    modal.style.display = "none";
}


closeM.addEventListener("click",closeModal);

b.addEventListener("click", event=>{
    modal.style.display = "block";
});

modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});


const fileInput = document.getElementById('file-input'),
      preview = document.getElementById('preview'),
      label = document.querySelector("#image_user"),
      text_delete = document.querySelector(".delete");

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (event) => {
        const image = document.createElement('img');
        image.src = event.target.result;
        image.style.maxWidth = "90%";
        image.style.maxHeight = "340px"
        image.style.position = "relative";
        image.style.left = "20px";
        image.style.top = "30px";
        preview.innerHTML = '';
        label.style.display = "none";
        text_delete.style.display = "inline-block"
        
        text_delete.addEventListener("click",e=>{
            preview.style.display = 'none';
            label.style.display = "block";
            text_delete.style.display = "none"
        });

        preview.appendChild(image);
        preview.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    preview.innerHTML = '';
    preview.style.display = 'none';
  }
});

