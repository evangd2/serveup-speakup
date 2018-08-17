const items = document.querySelectorAll("div.menu");

let item = null;

item = document.querySelector("div#Events");
item.style.backgroundImage = "url('/media/yellowflowers.png')";
// https://images.pexels.com/photos/768897/pexels-photo-768897.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#News");
item.style.backgroundImage = "url('/media/redflowers.png')";
// https://images.pexels.com/photos/1083895/pexels-photo-1083895.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Reps");
item.style.backgroundImage = "url('/media/purpleflowers.png')";
// https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Service");
item.style.backgroundImage = "url('/media/blueflowers.png')";

// https://i2.wp.com/www.onlygfx.com/wp-content/uploads/2017/07/blue-watercolor-brush-stroke-2-1.png')"
// https://images.pexels.com/photos/60005/forget-me-not-flower-meadow-wild-flower-60005.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";


item = document.querySelector("div#Home");
item.style.backgroundImage = "url('/media/greenflowers.png')";
// https:images.pexels.com/photos/580900/pexels-photo-580900.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')";

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
  console.log(items[i].style);
  originals[i] = items[i].style.backgroundImage;
  items[i].addEventListener("mouseover", function() {
    console.log("you hovered over item number " + i);
    console.log(items[i].style.backgroundImage);

    console.log("ID: " + items[i].id);
    const id = items[i].id;

    items[i].style.backgroundImage = "url('" + swappers[id] + "')";

    console.log(items[i].style.backgroundImage);
  });
}

console.log(originals);


for (let i = 0; i < items.length; i++) {
  items[i].addEventListener("mouseout", function() {
    console.log("you mouse out'ed out of item number " + i);
    items[i].style.backgroundImage = originals[i];

  });
}
