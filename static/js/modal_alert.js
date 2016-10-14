var AlertFunction = {
	open : function(msg, script) {
		// 활성화된 모달이 있는 경우 초기화한다.
		if ($('#modalPopup').length) {
			$('#modalPopup').modal('hide');
			$('#modalPopup').remove();
			$('.modal-backdrop').remove();
		}

		HtmlTemplate = '<div class="modal fade" id="modalPopup" tabindex="-1" role="dialog" aria-labelledby="modalPopup" aria-hidden="true">';
		HtmlTemplate += '    <div class="modal-dialog">';
		HtmlTemplate += '        <div class="modal-content">';
		HtmlTemplate += '            <div class="modal-header">';
		HtmlTemplate += '                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>';
		HtmlTemplate += '                <h4 class="modal-title">알림</h4>';
		HtmlTemplate += '            </div>';
		HtmlTemplate += '            <div class="modal-body">' + msg + '</div>';
		HtmlTemplate += '            <div class="modal-footer">';
		HtmlTemplate += '                <button type="button" class="btn btn-primary" onclick="' + script + ';">확인</button>';
		HtmlTemplate += '            </div>';
		HtmlTemplate += '        </div>';
		HtmlTemplate += '    </div>';
		HtmlTemplate += '</div>';
		$(document.body).append(HtmlTemplate);

		$('#modalPopup').modal('show');
		$('#modalPopup').on('hidden.bs.modal', function (e) {
			var Fn = new Function(script);
            Fn();

			$('#modalPopup').remove();
		});
	},

	confirm : function(msg, script) {
		// 활성화된 모달이 있는 경우 초기화한다.
		if ($('#modalPopup').length) {
			$('#modalPopup').modal('hide');
			$('#modalPopup').remove();
			$('.modal-backdrop').remove();
		}

		HtmlTemplate = '<div class="modal fade" id="modalPopup" tabindex="-1" role="dialog" aria-labelledby="modalPopup" aria-hidden="true">';
		HtmlTemplate += '    <div class="modal-dialog">';
		HtmlTemplate += '        <div class="modal-content">';
		HtmlTemplate += '            <div class="modal-header">';
		HtmlTemplate += '                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>';
		HtmlTemplate += '                <h4 class="modal-title">알림</h4>';
		HtmlTemplate += '            </div>';
		HtmlTemplate += '            <div class="modal-body">' + msg + '</div>';
		HtmlTemplate += '            <div class="modal-footer">';
		HtmlTemplate += '                <button type="button" class="btn btn-default" data-dismiss="modal">닫기</button>';
		HtmlTemplate += '                <button type="button" class="btn btn-primary" onclick="' + script + ';">확인</button>';
		HtmlTemplate += '            </div>';
		HtmlTemplate += '        </div>';
		HtmlTemplate += '    </div>';
		HtmlTemplate += '</div>';
		$(document.body).append(HtmlTemplate);

		$('#modalPopup').modal('show');
		$('#modalPopup').on('hidden.bs.modal', function (e) {
			$('#modalPopup').remove();
		});
	},

	close : function() {
		if ($('#modalPopup').length) {
			$('#modalPopup').modal('hide');
			$('#modalPopup').remove();
			$('.modal-backdrop').remove();
		}
	}
}