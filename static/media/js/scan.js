function progress_update(value) { 
    $('#progress').progressbar('option', 'value', value); 
    $('#percent').html(value + "%");
}

function monitor_progress() { 
    // Monitors the progress and updates the status and progress bars. 
    
        $.timer(1000, function(timer) {
            timer = timer; 
            $.get('/scan/status', function(data) { 
                var d = data.split(':');
                var in_progress = d[0];     // 1 if in progress, 0 if idle
                var percent = d[1];         // int
                var message = d.slice(2);   // rest of result is a message, even if it has a colon 

                // Update the progress bar.
                progress_update(percent);
                window.console.log('status: '+message.join(" "));
                $('#status').html(message.join(" ")); 
                
                if (message == 'Finished' || in_progress == 0) { 
                    timer.stop(); 
                    $('#buttons').html('<a href="#" id="start_scan">Start Scan</a>'); 
                }
                

            }); // $.get
        });     // $.timer
}

$(function(){
    $('#progress').progressbar({'value':0});
    $('#start_scan').live('click', function(e) { 
        // TODO: Make sure scan is not in progress before doing much!
        e.preventDefault();

        // Disable start scan link until scan is done.
        $('#buttons').html('<a href="#" id="stop_scan">Cancel Scan</a>'); 

        progress_update(1); 

        // Check here with .get if a scan is in progess.
        $.get('/scan/start'); 

        progress_update(10); 

        monitor_progress(); 

    });         // $('#start_scan').click()
});             // $(function(){})

