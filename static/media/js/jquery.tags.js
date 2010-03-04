jQuery.fn.addTag = function(scanid, tagname) {
    return this.each(function() {
        // Take a tag, and add it (with fadin) to the selected div.
        var $this = $(this);  //get a reference to the element BEFORE the callback.
        var flash = $(this).parent().children('.tag_flash');

        tagname = new String(tagname);
        cnt = tagname.split(' ').length;
        if (cnt > 1) {
            flash
                .hide()
                .html('Tags can only be one word!')
                .fadeIn(1000); 
        } else { 
            // First try to add the tag to the database:
            flash
                .hide()
                .html('Loading... please wait...')
                .fadeIn(1000); 
            url = '/scan/tag_add/'+scanid+'/'+tagname;
            $.get(url, function(data) {
                switch(data)
                {
                    case 'ok':
                        $('<span class="tag">'+tagname+'</span>')
                            .hide()
                            .appendTo($this)
                            .click(function(e){
                                e.preventDefault();
                                $this.delTag(scanid, tagname); 
                            })
                            .fadeIn(1000);
                            flash
                                .fadeOut(1000);
                        break;

                    case 'exists':
                        flash
                            .hide()
                            .html('That tag is already attached to this scan!')
                            .fadeIn(1000)
                            // FIXME: By suggestion of temp01 in #jquery
                            // replace fadeout with setTimeout.
                            // I just don't have time right now. Next release.
                            // Waiting altogether on this one...
                            // .fadeOut(30000);
                        
                        tag = $this.find("span.tag:contains('"+tagname+"')")
                        tag
                            // FIXME: This should all be a seperate jquery function for 
                            // flashing a tag. 
                            .animate({color: 'red'}, 500, function(){
                                tag.animate({color: 'black'}, 1000, function() {
                                    tag.animate({color: 'red'}, 500, function() {
                                        tag.animate({color: 'black'}, 1000, function() {
                                            tag.css('text-decoration', 'underline')    
                                        })    
                                    })
                                })        
                            });

                        break;
                    default:
                        msg = 'Something went wrong, please try again. Admin was notified.';
                        flash
                        .hide()
                            .html(msg)
                            .fadeIn(3000);
                } // end switch
            }); // end .get()
        } // end else
    }); // end this.each
}; // end jquery plugin function



jQuery.fn.delTag = function(scanid, tagname) { 
    // Removes a tag from a scan, but not the database, this is accomplished through admin.
    return this.each(function() {
        var $this = $(this);
        var flash = $(this).parent().children('.tag_flash');

        if (tagname.split(' ').length > 1) {
            flash
                .hide()
                .html('Tags can only be one word!')
                .fadeIn(3000); 

        } else {     
            // Try to delete tag.
            flash
                .hide()
                .html('Loading... Please wait...')
                .fadeIn(1000); 
            url = '/scan/tag_del/'+scanid+'/'+tagname;
            $.get(url, function(data) { 
                    switch(data)
                    {
                        case 'ok':
                            // Remove tag from list.
                            $this
                                .find("span.tag:contains('"+tagname+"')")
                                .css('color', 'red')
                                .fadeOut('slow');
                            flash
                                .html('Tag deleted!')
                                .fadeOut(1000);
                    }

            }); // end .get()
        } // end else
    }); // end this.each
}; // end jquery plugin function
