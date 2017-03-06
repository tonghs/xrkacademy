$('a.anchor').click((event)->
    targetId = $(this).attr('href').replace('#','')
    $("html, body").animate({scrollTop: $('a[name=' + targetId + ']').offset().top}, 800)
)
