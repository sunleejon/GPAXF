function parse_data() {
    var $password_input = $("#password_input");
    var password = $password_input.val().trim();
    $password_input.val(md5(password));
    return true
}

// 5f93f983524def3dca464469d2cf9f3e
// 5f93f983524def3dca464469d2cf9f3e