$(document).on('turbolinks:load', function() {
  var path     = location.pathname;
  var users = $('.users');

  function buildHTML(user) {
    var html = $('<div class="col s3 user">');
    if (user.image) {
      if (user.attend_group) {
       html.append('<img class="circle responsive-img" src=' + user.image + '>');
      } else {
        html.append('<img class="circle responsive-img user--undecided" src=' + user.image + '>');
      }
    }
    html.append('<h6 class="center black-text">名前: ' + user.name + '</h6>' + '<h6 class="center black-text">年齢: ' + user.age + '</h6>' + '<h6 class="center black-text">職業: ' + user.job + '</h6>')
    return html;
  }

  if (path.match('/groups/')) {
    if (window.set_timer_on == null) {
      window.timer = setInterval(function(){
        $.ajax({
          type:     'GET',
          url:       path,
          dataType: 'json'
        })
        .done(function(data) {
          users.empty()
          var existedUserIds = users.children().map(function(i, elm) {
            return Number(elm.dataset.userId);
          });
          $.each(data, function(i, user) {
            var html = buildHTML(user);
            users.append(html);
          });
        });
      }, 5000);
    }
  } else if (window.set_timer_on !== null) { // setIntarvalを動かしたくないページに来てtimerが動いる場合
    clearInterval(window.timer)
    window.timer = null
  }
});
