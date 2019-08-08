$(function() {
  // Get handle to the chat div
  var $chatWindow = $('#messages');

  // Our interface to the Chat service
  var chatClient;

  // A handle to the "general" chat channel - the one and only channel we
  // will have in this sample app
  var generalChannel;

  // The server obtain the username of logged in user - store that value
  // here
  var username;

  // Helper function to print info messages to the chat window
  function print(infoMessage, asHtml) {
    var $msg = $('<div class="info">');
    if (asHtml) {
      $msg.html(infoMessage);
    } else {
      $msg.text(infoMessage);
    }
    $chatWindow.append($msg);
  }

  // Helper function to print chat message to the chat window
  function printMessage(fromUser, message) {
    var $user = $('<span class="username">').text(fromUser + ':');
    if (fromUser === username) {
      $user.addClass('me');
    }
    var $message = $('<span class="message">').text(message);
    var $container = $('<div class="message-container">');
    $container.append($user).append($message);
    $chatWindow.append($container);
    $chatWindow.scrollTop($chatWindow[0].scrollHeight);
  }

  // Alert the user they have been logged in
  print('Attempting to log in. If username does not display within a few more seconds, then you do not have permission to chat in this room. Please contact site admin for assistance...');

  // Get an access token for the current user, passing a username (identity)
  // and a device ID - for browser-based apps, we'll always just use the
  // value "browser"
  $.getJSON('/token', {
    device: 'browser'
  }, function(data) {


    // Initialize the Chat client
    Twilio.Chat.Client.create(data.token).then(client => {
      console.log('Created chat client');
      chatClient = client;
      chatClient.getSubscribedChannels().then(createOrJoinGeneralChannel);

    // Alert the user they have been logged in
    username = data.identity;
    print('You are logged in to chat: '
    + '<span class="me">' + username + '</span>', true);

    }).catch(error => {
      console.error(error);
      print('There was an error creating the chat client:<br/>' + error, true);
      print('Please check your .env file.', false);
    });
  });

  function createOrJoinGeneralChannel() {
    // Get the general chat channel, which is where all the messages are
    // sent in this simple application
    print('Welcome to the chat. Proceed to chat...');
    const chatroomSlug = $chatWindow.data('chatroom')
    console.log("chatroom", chatroomSlug)
    chatClient.getChannelByUniqueName(chatroomSlug)
    .then(function(channel) {
      generalChannel = channel;
      console.log('Found general channel:');
      console.log(generalChannel);
      setupChannel();
    }).catch(function() {
      // If it doesn't exist, let's create it
      console.log('Creating channel');
      chatClient.createChannel({
        uniqueName: chatroomSlug,
        friendlyName: 'General Chat Channel'
      }).then(function(channel) {
        console.log('Created channel:');
        console.log(channel);
        generalChannel = channel;
        setupChannel();
      }).catch(function(channel) {
        console.log('Channel could not be created:');
        console.log(channel);
      });
    });
  }

  // Set up channel after it has been found
  function setupChannel() {
    // Join the general channel
    generalChannel.join().then(function(channel) {
      print('Joined channel as '
      + '<span class="me">' + username + '</span>.', true);
    });

    // Get Messages for a previously created channel
    generalChannel.getMessages().then(function(messages) {
        const totalMessages = messages.items.length;
        for (i = 0; i < totalMessages; i++) {
          const message = messages.items[i];
          printMessage('Chat History ' + message.author, message.body);
        }
        console.log('Total Messages:' + totalMessages);
    });

    // Listen for new messages sent to the channel
    generalChannel.on('messageAdded', function(message) {
      printMessage(message.author, message.body);
    });
  }

  // Send a new message to the general channel
  var $input = $('#chat-input');
  $input.on('keydown', function(e) {

    if (e.keyCode == 13) {
      if (generalChannel === undefined) {
        print('The Chat Service is not configured for you. Please contact admin for assistance.', false);
        return;
      }
      generalChannel.sendMessage($input.val())
      $input.val('');
    }
  });
});
