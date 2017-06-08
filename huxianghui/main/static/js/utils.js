$(function () {

	$('.hold_view form').on('submit', function (e) {
		var self = this
		e.preventDefault()
		var formData = new FormData(self)
		formData.set("password0",$.md5(formData.get("password0")))
        formData.set("password1",$.md5(formData.get("password1")))
        console.log($.md5(formData.get("password0")))
		$.ajax({
			url: $(self).attr('action'),
			type: $(self).attr('method'),
			data: formData,
			processData: false,
			contentType: false,
			success: function (res) {
				console.log('success')
				console.log(res)
				$(document).find("html").html(res);
                setTimeout(function () {window.location.href = '/reg_login.html'}, 2000)
			},
			error: function (xhr) {
				console.log('failed')
				console.log(xhr)
			}
		})
	})


})