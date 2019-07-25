$(function (){

  var loadform = function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
	  beforeSend: function(){
	    $("#modal-contact").modal("show");
	   },
      success: function(data){
        $("#modal-contact .modal-content").html(data.html_form);
      },
    });
  };

  var saveform = function(){
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#contact .album").html(data.html_contact_list); // <-- it updates the album with the newly created contact
          $("#modal-contact").modal("hide");  // <-- Close the modal          
        }
        else {
          $("#modal-contact .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // create contact
  $(".js-create-contact").click(loadform);
  $("#modal-contact").on("submit", ".js-contact-create-form",saveform);

  // Update contact
  $("#contact").on("click", ".js-contact-update",loadform);
  $("#modal-contact").on("submit", ".js-book-update-form",saveform);

  // delete contact
  $("#contact").on("click", ".js-contact-delete",loadform);
  $("#modal-contact").on("submit", ".js-contact-delete-form",saveform);

});