$(document).ready(function () {
    // Show/hide the file input for image upload
    $('#image-upload-btn').on('click', function () {
        $('.custom-file').toggle();
    });

    // Send message in group or private chat
    $('#send-btn').on('click', function () {
        var content = $('#message-input').val().trim();
        var groupId = $('#group-id').val();

        // Check if groupId is undefined and set it to null
        groupId = groupId === 'undefined' ? null : groupId;

        // FormData to send text and image data
        var formData = new FormData();
        formData.append('content', content);
        formData.append('group_id', groupId);

        var imageInput = $('#image-input')[0];
        var image = imageInput.files.length > 0 ? imageInput.files[0] : null;
        formData.append('image', image);

        // Send the message via AJAX
        $.ajax({
            type: 'POST',
            url: '/chat/private/send_message/',
            data: formData,
            contentType: false,
            processData: false,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function (data) {
                if (data.status === 'ok') {
                    // Clear the input field
                    $('#message-input').val('');

                    // Append the new message to the chat container
                    var messageContainer = $('#chat-container');
                    var newMessage = $('<div class="message">' +
                        '<p>' + data.sender + ' - ' + data.timestamp + '</p>' +
                        (data.content ? '<p>' + data.content + '</p>' : '') +
                        (data.image ? '<img src="' + data.image + '" alt="Image">' : '') +
                        '</div>');
                    messageContainer.append(newMessage);
                } else {
                    console.error('Error sending message:', data.message);
                }
            },
            error: function (error) {
                console.error('Error sending message:', error);
            }
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Check if the cookie name matches the target name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
});
