$.ajaxSetup({
            beforeSend:function (xhr,settings) {
                xhr.setRequestHeader("X-CSRFtoken",$.cookie("csrftoken"))
            }
        });