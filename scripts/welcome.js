const items = document.querySelectorAll("div.menu");

// alert(items.length);


// const navItems = document.querySelectorAll("News");
//
// alert(navItems.length)

// items.forEach(item => item.addEventListener("hover", show));

let item = null;

item = document.querySelector("div#Events");
item.style.backgroundImage = "url('https://images.pexels.com/photos/768897/pexels-photo-768897.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#News");
item.style.backgroundImage = "url('https://images.pexels.com/photos/1083895/pexels-photo-1083895.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Reps");
item.style.backgroundImage = "url('https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Service");
item.style.backgroundImage = "url('https://images.pexels.com/photos/60005/forget-me-not-flower-meadow-wild-flower-60005.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Home");
item.style.backgroundImage = "url('https://images.pexels.com/photos/580900/pexels-photo-580900.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";

swappers = {
  "Events": "/media/colorevents.png",
  "News": "/media/colornews.png",
  "Service": "/media/colorheart.png",
  "Reps": "/media/colorreps.png",
  "Home": "/media/colorhome.png",
}




var originals = []
for (let i = 0; i < items.length; i++) {
  originals[i] = "";
}
console.log(originals);

for (let i = 0; i < items.length; i++) {
  // alert("HELLO: " + i);
  console.log(items[i].style);

  // Save the original image to be restored on mouseout
  originals[i] = items[i].style.backgroundImage;

  // Add listener to each element on mouseover
  items[i].addEventListener("mouseover", function() {
    console.log("you hovered over item number " + i);
    console.log(items[i].style.backgroundImage);

    console.log("ID: " + items[i].id);
    const id = items[i].id;

    // items[i].style.backgroundImage = "url('/media/events.png')";
    items[i].style.backgroundImage = "url('" + swappers[id] + "')";
    // items[i].style.width = "100%";
    // items[i].style.height = "100%";

    console.log(items[i].style.backgroundImage);
    // items[i].style.width = "0px";
  });
}

console.log(originals);


for (let i = 0; i < items.length; i++) {
  // alert("HELLO: " + i);
  items[i].addEventListener("mouseout", function() {
    console.log("you mouse out'ed out of item number " + i);
    items[i].style.backgroundImage = originals[i];
    // items[i].style.width = "50%";
    // items[i].style.height = "50%";
  });
}
//
// function show(event) {
//   alert("hello");
//   const filename = event.target.innerHTML;
//     content.innerHTML = `<img src="events.png">`;
// }
