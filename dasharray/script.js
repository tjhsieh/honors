

var svg = document.querySelector('svg#sign');

var pathes = svg.querySelectorAll('.path');

var lengths = [];

var speed = 1000;

function repeat() {
  lengths = [];

  pathes.forEach(function (el, i) {
    var len = el.getTotalLength();
    console.log('i = ' + i);
    console.log('len = ' + len);

    lengths.push(len);

    //lengths.forEach(function(element) {
    //  console.log(element);
    //});

    //console.log('lengths = ' + lengths);

    el.setAttribute('stroke-dasharray', len);
    el.setAttribute('stroke-dashoffset', len);

    setTimeout(function () {
      el.style.transition = "stroke-dashoffset ".concat(len / speed, "s linear");

      //console.log("stroke-dashoffset ".concat(len / speed, "s linear"));

      el.addEventListener('transitionend', function () {
        draw(i + 1);
        console.log( 'draw(' + i+1 + ');');
      });
    }, 1);

  });

}


function draw(i) {
  if (i >= pathes.length) {
    //return;
    draw(0);
  }

  //pathes[i].setAttribute('stroke-dashoffset', 0);
}


function reset() {
  pathes[0].setAttribute('stroke-dashoffset', 0);
  pathes[1].setAttribute('stroke-dashoffset', 0);
  pathes[2].setAttribute('stroke-dashoffset', 0);
  pathes[3].setAttribute('stroke-dashoffset', 0);
  pathes[4].setAttribute('stroke-dashoffset', 0);
}

setInterval(reset, 5000);

setInterval(repeat, 4000);
/*
setInterval(draw(0), 1000);
setInterval(draw(1), 2000);
setInterval(draw(2), 1000);
setInterval(draw(3), 2000);
setInterval(draw(4), 1000);
*/

