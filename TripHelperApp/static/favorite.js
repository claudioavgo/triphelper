/* when a user clicks, toggle the 'is-animating' class */
$(".fav").on('click touchstart', function(){
    $(this).toggleClass('is-animating');
  });
  
  /*when the animation is over, remove the class*/
  $(".fav").on('animationend', function(){
    $(this).toggleClass('is-animating');
  });
  