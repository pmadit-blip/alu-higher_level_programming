$(document).ready(function () {
  function translate () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(translate);
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});
