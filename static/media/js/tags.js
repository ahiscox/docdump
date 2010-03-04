/**
 * Handles adding, deleting, and manipulation of tags.
 */

/**
 * Update all tag editors on the page with the list in
 * div#alltags. 
 */
function updateTags() {

    // grab list
    var list = $('div#alltags').text().split(',');
    // for each tag in list, update select boxes.

    var html = ""
    for (var tag in list) {
        html = html+"<option>"+list[tag]+"</option>"
    }

    $('select.alltags').html(html);


    // Update open input boxes too.
    var inputbox = $('form').find('input');
    inputbox.val('Click here to type a tag')
     
}

/**
 * TAG EVENT HANDLERS
 */

function handler_tag_button() {
    $('a.t_tags').live('click', function(e){
        e.preventDefault();

        var ocr = $(this).parents('.result').find('.ocr')
        ocr
            .html('Loading')

        var scanid = $(this).parents('.result').attr('id');
        $.get('/scan/tag_form/' + scanid, function(){
            updateTags();
        });
    });
}

function handler_tag_delete() {
   $('span.tag').live('click', function(e){
            e.preventDefault(); 

            var tagname = $(this).html();  
            var scanid = $(this).parents('.result').attr('id');
            var attached_tags = $(this).parents('.result').find('.attached_tags');
            attached_tags.delTag(scanid, tagname); 
    }); 
}

function handler_tag_select() {
    $('select.alltags').live('click', function(e){
        // Disable select until we're done.
        $(this).attr('disabled','disabled'); 

        // Grab scanid and tagname
        var scanid = $(this).parents('.result').attr('id');
        var tagname = $(this).val();

        var attached_tags = $(this).parents('.result').find('.attached_tags');

        attached_tags
            .addTag(scanid, tagname);

        // Enable select again. 
        $(this).attr('disabled', false); 
    });
}

function handler_tag_input(){ 
    // handlers for tag input box.
    // First set a default string
    // FIXME: This should be removed, and just 
    // set in the taconite xml doc. 
    var inputbox = $('form').find('input');
    inputbox
        .val('Click here to type a tag')
        .live('click', function(e){
                e.preventDefault();
                
                $(this).focus();
                $(this).val('');
        });

    $('.tag_input form').live('submit', function(e){
            e.preventDefault();
            var inputbox = $(this).find('input'); 
            
            inputbox.focus();
           
            var scanid = $(this).parents('.result').attr('id');
            var tagname = inputbox.val();
            var attached_tags = $(this).parents('.result').find('.attached_tags');
            attached_tags.addTag(scanid, tagname);
            inputbox.val('');
    });
}

function updateTagHandlers() { 
    handler_tag_button(); 
    handler_tag_delete();
    handler_tag_select();
    handler_tag_input();
}

$(function () { 
    updateTagHandlers();
}); 

