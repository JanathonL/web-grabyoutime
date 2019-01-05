$('.message .close').on('click', function () {
    $(this).closest('.message').transition('fade');
});
// $('.dropdown').dropdown();

function Search() {
    var val = $('#search').val();
    if (!val) {
        alert('no project')
        return
    }
    else {
        window.location = '/projects/?query=' + val;
    }
   
}
$('#search_icon').click(Search);

function RefreshMessage() {
  $.get("/get_message/")
  .done(function(data) {
      
      var msgNumber = $("#msgNumber");
      var size = data['number'] 
      msgNumber.html(size); 
  });
}

$(document).ready(function () {
  RefreshMessage()
  window.setInterval(RefreshMessage, 5000);
  // CSRF set-up copied from Django docs
  function getCookie(name) {  
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});