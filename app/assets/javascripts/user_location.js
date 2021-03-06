$(document).on('turbolinks:load', function() {
  var path = location.pathname;
  if (path == '/') {
    /***** ユーザーの現在の位置情報を取得 *****/
    function successCallback(position) {
      var locationData = { coordinate :{ latitude: position.coords.latitude, longitude: position.coords.longitude } }
      $.ajax({
        type:        'POST',
        url:         '/events/search',
        data:        locationData,
        dataType:    'script'
      })
    }

    /***** 位置情報が取得できない場合 *****/
    function errorCallback(error) {
      var err_msg = "";
      switch(error.code)
      {
        case 1:
          err_msg = "位置情報の利用が許可されていません";
          break;
        case 2:
          err_msg = "デバイスの位置が判定できません";
          break;
        case 3:
          err_msg = "タイムアウトしました";
          break;
      }
      document.getElementById("show_result").innerHTML = err_msg;
      //デバッグ用→ document.getElementById("show_result").innerHTML = error.message;
      // ToDo ここの例外処理
    }


    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
  }
});
