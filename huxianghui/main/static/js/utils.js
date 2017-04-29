$(function () {

	$('form.form-container').on('submit', function (e) {
		var self = this
		e.preventDefault()
		var formData = new FormData(self)
		$.ajax({
			url: $(self).attr('action'),
			type: $(self).attr('method'),
			data: formData,
			processData: false,
			contentType: false,
			success: function (res) {
				console.log('success')
				console.log(res)
				$('.msg').show()
				// setTimeout(function () {window.location.href = '/'}, 1000)
			},
			error: function (xhr) {
				console.log('failed')
				console.log(xhr)
				if (xhr.status === 403) {
					alert('无权作此操作, 请联系管理员')
				}
				let json = xhr.responseJSON

				for (let i of ['email', 'phone', 'name', 'grade', 'campus']) {
					if (json[i]) {
						$('[name={0}]'.format(i)).toggleClass('error')
					}
				}
			}
		})
	})


})