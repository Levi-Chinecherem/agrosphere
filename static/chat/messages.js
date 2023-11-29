$(document).ready(function () {
  const userSwitch = $('input[name="communicationSwitch"]');
  const searchBar = $('#search-bar');
  const searchBtn = $('#search-btn');
  const userList = $('#user-list');

  // Initial load of communicated users
  loadUsers('communicated');

  // Switcher event listener
  userSwitch.on('change', function () {
      const switchValue = userSwitch.val();
      loadUsers(switchValue);
  });

  // Search button event listener
  searchBtn.on('click', function () {
      const searchTerm = searchBar.val().trim();
      const switchValue = userSwitch.val();
      searchUsers(searchTerm, switchValue);
  });

  // Function to load users based on switch value
  function loadUsers(switchValue) {
      // Clear user list
      userList.empty();

      // Make an AJAX request to the server to get the users
      $.getJSON(`/get_users/?switch_value=${switchValue}`)
          .done(function (data) {
              data.forEach(function (user) {
                  const userCard = createUserCard(user);
                  userList.append(userCard);
              });
          })
          .fail(function (error) {
              console.error('Error fetching users:', error);
          });
  }

  // Function to search users
  function searchUsers(searchTerm, switchValue) {
      // Clear user list
      userList.empty();

      // Make an AJAX request to the server to search users
      $.getJSON(`/search_users/?search_term=${searchTerm}&switch_value=${switchValue}`)
          .done(function (data) {
              data.forEach(function (user) {
                  const userCard = createUserCard(user);
                  userList.append(userCard);
              });
          })
          .fail(function (error) {
              console.error('Error searching users:', error);
          });
  }

  // Function to create a user card
  function createUserCard(user) {
      const card = $('<div>').addClass('col-md-4 mb-3').html(`
          <div class="card">
              <div class="card-body d-flex">
                  ${user.profile.image
                      ? `<img src="${user.profile.image}" alt="${user.username}" class="rounded-circle mr-3" style="width: 50px; height: 50px;">`
                      : ''}
                  <div>
                      <h5 class="card-title">${user.username}</h5>
                      <p class="card-text">Occupation: ${user.profile.occupation}</p>
                      <!-- Add any other details about the user here -->
                      <a href="{% url 'private_chat' user.id %}" class="btn btn-primary mt-2">Send Message</a>
                  </div>
              </div>
          </div>
      `);
      return card;
  }
});
