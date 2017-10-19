(function () {
    app = {};
    app.init = function () {
        $('a.ajax-popup').on('click', function () {
            return !app.ajaxLoad('popup', this.href, '', function (res) {
                if (res) $('div.shadow-black').show('fast', function () {
                    $('div.b-instagram-popup').show();
                });
            });
        });
    };
    app.ajaxLoad = function (target, url, data, callback) {
        var $t = $('#' + target);
        if (!$t.length) {
            return false;
        }
        callback = callback || app.fadeIn;
        $t.load(url, data, callback);
        return true;
    };
    app.fadeIn = function () {
        $(this).css('opacity', 0).fadeTo('fast', 1);
    }
})();
$(app.init);
$('a[rel~=async]').live('click', function () {
    var target = $(this).data('target') || this.target;
    return !app.ajaxLoad(target, this.href);
});