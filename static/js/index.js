// Video
function handleVideo(url) {
  const bg = document.createElement("video")
  bg.src=url
  bg.autoplay=true
  bg.muted=true
  bg.loop=true
  document.querySelector("body").prepend(bg)
  document.querySelector("video").play()
}

function getVideo() {
  const url = "https://pixabay.com/api/videos/?key=16348363-5f62afc96e1c40cb93593dede&q=coding"
  fetch(url).then(response => {
    response.json().then(result => {
      // const videoArray = result["hits"]
      urlArray = [
      "https://player.vimeo.com/external/334950213.hd.mp4?s=09b7862b8b20d009ef6eb494e1a8683919ca7947&profile_id=175",
      "https://player.vimeo.com/external/179738669.hd.mp4?s=fba5ab918251dfe26454fad90b3a535943df960a&profile_id=119",
      "https://player.vimeo.com/external/148614367.hd.mp4?s=551ae2fc0254f99f43f0a6126b8e4d0666fba327&profile_id=119",
      // "https://player.vimeo.com/external/255797028.hd.mp4?s=1350edf54cc5e84c8e154e992e5e7d53a5e46a7d&profile_id=175",
      "https://player.vimeo.com/external/369325356.hd.mp4?s=64e50b1b0f83ce9500a319bc9b31556761efd988&profile_id=175"
    ]
      const index = Math.floor(Math.random() * urlArray.length)
      const videoURL = urlArray[index]
      console.log(videoURL);
      handleVideo(videoURL)
    })
  })
}
getVideo()
// const resultBody = document.querySelector(".report").classList.add("black")

// Paint List
const div = document.querySelector(".js-added");
const list = div.querySelector("ul");
const form = document.querySelector(".js-add-form");
const addedForm = document.getElementById("js-term")
const userInput = form.querySelector("input");
const ADD_STORAGE = "terms";

let termList = [];
let queryList = [];

function saveTodo(obj) {
    localStorage.setItem(ADD_STORAGE, JSON.stringify(obj))
}

function handleSubmit(e) {
    e.preventDefault();
    const text = userInput.value;
    paintList(text)
    userInput.value = "";
}

function handleDelete(e) {
    console.log(e.target.parentNode.id)
    list.removeChild(e.target.parentNode)
    const updatedArray = termList.filter(element => {
        return element.id !== parseInt(e.target.parentNode.id)
    })
    console.log(updatedArray)
    termList = updatedArray
    saveTodo(termList)
}

function paintList(text) {

    const term = document.createElement("li");
    const DEL_BTN = document.createElement("i");
    // const hiddenInput = document.createElement("input")
    const id = termList.length + 1
    term.id = id
    // hiddenInput.name = "term"
    // hiddenInput.classList.add("hiding")
    // addedForm.classList.add(text)
    // term.nodeName = text
    // term.name = text
    DEL_BTN.classList.add("fas")
    DEL_BTN.classList.add("fa-times-circle")
    DEL_BTN.classList.add("del-btn-size")
    DEL_BTN.addEventListener("click", handleDelete)

    term.innerText = `${text} `;
    term.appendChild(DEL_BTN);
    // list.appendChild(hiddenInput)
    list.appendChild(term);
    const obj = {
        id : id,
        text: text,
    }
    termList.push(obj);
    
    saveTodo(termList)

}
// window.addEventListener("change", ()=> {

// })
// data.addEventListener("change",()=> {
//   if (termList.length === 0) {
//     list.classList.add("hiding")
//   } else {
//     list.classList.remove("hiding")
//   }
// })
function loadData() {
    const data = localStorage.getItem(ADD_STORAGE);

    // const finishedData = localStorage.getItem(FINISHED_STORAGE);
    if (data !== null) {
        JSON.parse(data).forEach(element => {
            paintList(element.text);
        })
    }
}
form.addEventListener("submit", handleSubmit)

function disableBtn() {
  const btn = addedForm.querySelector("button")
  const loading = new Image()
  loading.src = "https://i.ya-webdesign.com/images/loading-png-gif.gif"
  loading.width = "30"
  loading.height = "30"
  btn.innerText = ""
  btn.style.background = "none"
  btn.style.outline = "none"
  btn.style.border = "none"
  btn.style.cursor = "wait"
  btn.appendChild(loading)
  btn.classList.remove("btn")
  btn.classList.remove("btn-dark")
  btn.classList.add("disabled")
}

function noticeUser(str) {
  document.querySelector(".notice").innerHTML = "Wait a second plz,<br>Scrapping..."
  const message = form.querySelector(".search-term")
  message.innerHTML = `Pulling latest remote job list<br>[ ${str}]<br>from<br>WeWork / StackOverflow / RemoteOK`
  const mainBoxInput = form.querySelector("input")
  const mainBoxButton = form.querySelector("button")
  mainBoxInput.classList.add("hiding")
  mainBoxButton.classList.add("hiding")
  disableBtn()
}

function handleReport(e) {
  const li = document.querySelectorAll("li")
  let str = ""
  for (let i=0; i<li.length; i++) {
    str += li[i].textContent
  }
  // console.log(str);
  addedForm.querySelector("input").setAttribute("value", str)
  // console.log(e.target.parentNode);
  noticeUser(str)
}

addedForm.querySelector("button").addEventListener("click", handleReport)

loadData();
