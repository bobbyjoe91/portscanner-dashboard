setInterval(function () {
   $.ajax({
      method: "GET",
      url: "{% url 'get_more_tables' %}",
      success: function (data) {
         $("tbody").empty();
         $.each(data, function (key, value) {
            var iP = ip;
            var port = value.port;
            var status = value.status;
            var timeStamp = value.timeStamp;
            $("tbody").append(
               "<tr><td>" + iP + "</td><td>" + port + "</td><td>" + status + "</td><td>" + timeStamp + "</td></tr>"
            )
         })
      },
      error: function (data) {
         console.log("error")
         console.log(data)
      }
   })
}, 1000)