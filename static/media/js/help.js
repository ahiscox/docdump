/**
 * Help dialog initialization
 * @return
 */
function helpInit() {
	$('#help').dialog({
		modal: true,
		width: 400,
		height: 450,
		position: ['right', 'top'],
		/**
		 * This overlay setting doesn't seem to change a damn thing.
		 * I got it from the API and someone on irc.freenode.net/jquery 
		 * Commenting it out until the correct setting can be found.
		 *
		overlay: {
	    	opacity: .5,
	        background: 'black'
	    },*/
	    title: 'To close help, press "Esc" key.'
	    // show: 'slide'
	});
	$('#help').dialog('open');
}

/**
 * Load the help index.
 */
function helpIndex() {
	$.get('/help/topic/index');
}

/**
 * HELP EVENT HANDLERS
 */
$(function () {

	/**
	 * HELP BUTTON
	 * Opens the help dialog and navigates to index.
	 */
	$('a.help').live('click', function(e){
		e.preventDefault();
		helpInit();
		helpIndex();
	});

	/**
	 * HELP INDEX
	 * Navigate to help index. (Used in menus)
	 */
	$('#dochome').live('click', function(e){
		e.preventDefault();
        helpIndex();
	});
});
