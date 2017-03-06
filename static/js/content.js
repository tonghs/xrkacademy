(function() {
  $('a.anchor').click(function(event) {
    var targetId;
    targetId = $(this).attr('href').replace('#', '');
    return $("html, body").animate({
      scrollTop: $('a[name=' + targetId + ']').offset().top
    }, 800);
  });

}).call(this);
