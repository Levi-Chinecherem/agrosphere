document.addEventListener('DOMContentLoaded', function () {
    // Add event listener for chat button
    const chatButtons = document.querySelectorAll('.chat-button');

    chatButtons.forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            const recipientId = this.getAttribute('data-recipient-id');
            
            // Check if the recipient is not the same as the logged-in user
            if (recipientId !== '{{ request.user.id }}') {
                // Redirect to the private chat page
                window.location.href = `/private-chat/${recipientId}/`;
            } else {
                // Optionally, display a message or handle the case where the user is trying to chat with themselves
                alert('You cannot chat with yourself.');
            }
        });
    });


    
    // Add event listener for like button
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            likePost(postId);
        });
    });

    function likePost(postId) {
        fetch(`/like-post/${postId}/`)
            .then(response => response.json())
            .then(data => {
                const likeCountElement = document.querySelector(`.like-count[data-post-id="${postId}"]`);
                likeCountElement.textContent = data.like_count;
    
                const likeButton = document.querySelector(`.like-button[data-post-id="${postId}"]`);
                likeButton.textContent = data.is_liked ? 'Unlike' : 'Like';
            })
            .catch(error => console.error('Error liking post:', error));
    }


    // Add event listener for share button
    const shareButtons = document.querySelectorAll('.share-button');

    shareButtons.forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            sharePost(postId);
        });
    });

    function sharePost(postId) {
        // Call the share post endpoint in the sharing app
        fetch(`/sharing/share-post/${postId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    alert('Post shared successfully.');
                } else {
                    alert('Error sharing post: ' + data.message);
                }
            })
            .catch(error => console.error('Error sharing post:', error));
    }



    // Floating Create Post Button
    const createPostButton = document.querySelector('.create-post-button');

    createPostButton.addEventListener('click', function () {
        // Handle the click event for the create post button
        // You may want to redirect to the create post page
        // Replace the window.location.href with the appropriate URL
        window.location.href = '/create/';
    });
});
