$(function () {

 // $.taconite.debug = false;

  // Show large image when thumbnail is clicked.
  $('img.thumbnail').click(function(){
    img = $(this).parent().attr('href');
    html = '<img src="' + img + '" />'
    $('#dialog').html(html);
    dialog_setup = {
      modal: true,
      overlay: {
        opacity: 0.5
      },
      width: 1024,
      title: 'Large Preview, to close press "Esc" key.',
      position: 'top'
    };
    $('#dialog').dialog(dialog_setup).dialog('open');
    return false;
  });

  // Display (and add) comments for individual scan.
  $('a.t_comments').click(function(e){
    e.preventDefault();

    // Get ID of current scan.
    scanid = $(this).parents('.result').attr('id');
    $.get('/scan/comments/' + scanid);
  });

  $('a.t_excerpt').click(function(e){
    e.preventDefault();

    scanid = $(this).parents('.result').attr('id');
    $.get('/scan/excerpt/' + scanid);

  });
}); // End of $() events.
