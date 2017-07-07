$(document).on('turbolinks:load', function() {
  var path     = location.pathname;
  var users = $('.users');

  function buildHTML(user) {
    var html = $('<div class="col s3 user" data-user-id=' + user.id + '>');
    if (user.image) {
      html.append('<img class="circle responsive-img" src=' + user.image + '>');
    }
    html.append('<h6 class="center black-text">名前: ' + user.name + '</h6>' + '<h6 class="center black-text">年齢: ' + user.age + '</h6>' + '<h6 class="center black-text">職業: ' + user.job + '</h6>')
    return html;
  }

  if (path.match('/groups/')) {
    var timer = setInterval(function(){
      $.ajax({
        type:     'GET',
        url:       path,
        dataType: 'json'
      })
      .done(function(data) {
        var existedUserIds = users.children().map(function(i, elm) {
          return Number(elm.dataset.userId);
        });
        $.each(data, function(i, user) {
          if ($.inArray(user.id, existedUserIds) === -1) {
            var html = buildHTML(user);
            users.append(html);
         }
        });
      });
    }, 5000);
  }
  // turbolinks によってページ遷移先にsetIntervalが引き継がれてしまうバグを解除
  $(this).on('turbolinks:click', function() {
    clearInterval(timer);
  });
});
