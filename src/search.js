let conversations = [];

fetch('conversations.json')
  .then(response => response.json())
  .then(data => {
    conversations = data;
  });

function checkIfNpcNameQuery(conv, queryLower) {
  for (const line of conv.conversation) {
    const speaker = Object.keys(line)[0];
    if (speaker.toLowerCase() === queryLower && speaker !== "Player") {
      return true;
    }
  }
  return false;
}

function displayNPCConversations(queryLower) {
  const results = [];

  for (const conv of conversations) {
    if (checkIfNpcNameQuery(conv, queryLower)) {
      displayWholeConversation(conv, results);
    }
  }

  displayResults(results);
}

function displayWholeConversation(conv, results) {
  const conversationText = conv.conversation
    .map((line) => {
      const speaker = Object.keys(line)[0];
      return `${speaker}: ${line[speaker]}`;
    })
    .join("\n");

  if (!results.includes(conversationText)) {
    results.push(conversationText + "\n");
  }
}

function displayResults(results) {
  const searchResultsElement = document.getElementById("search-results");
  if (results.length === 0) {
    searchResultsElement.innerHTML = "<p>No results found.</p>";
  } else {
    searchResultsElement.innerHTML = results
      .map((result) => "<pre>" + result + "</pre>")
      .join("\n\n");
  }
}


function search(query) {
  const queryLower = query.toLowerCase();
  const results = [];

  let isNpcName = false;
  for (const conv of conversations) {
    if (checkIfNpcNameQuery(conv, queryLower)) {
      isNpcName = true;
      break;
    }
  }

  for (const conv of conversations) {
    const conversationResult = processConversation(conv, queryLower, isNpcName);
    if (conversationResult.length > 0) {
      const resultString = conversationResult.join('\n') + '\n';
      if (!results.includes(resultString)) {
        results.push(resultString);
      }
    }
  }
  
  displayResults(results);
}

function processConversation(conv, queryLower, isNpcName) {
  const conversationResult = new Set();

  for (let i = 0; i < conv.conversation.length; i++) {
    const line = conv.conversation[i];
    const speaker = Object.keys(line)[0];
    const text = line[speaker];
    const lineLower = text.toLowerCase();

    let found = false;

    if (isNpcName) {
      const isTargetNpc = speaker.toLowerCase() === queryLower;
      const mentionsTargetNpc = lineLower.includes(queryLower) && speaker !== "Player";
      found = isTargetNpc || mentionsTargetNpc;
    } else {
      const isPlayerQuery = speaker === 'Player' && lineLower.includes(queryLower);
      const isNpcResponse = speaker !== 'Player' && lineLower.includes(queryLower);
      found = isPlayerQuery || isNpcResponse;
    }

    if (found) {
      let startIndex = 0;
      for (let j = i - 1; j >= 0; j--) {
        if (conv.conversation[j].Player) {
          startIndex = j;
          break;
        }
      }

      for (let j = startIndex; j <= i; j++) {
        const currentLine = conv.conversation[j];
        const currentSpeaker = Object.keys(currentLine)[0];
        const currentText = currentLine[currentSpeaker];
        conversationResult.add(`${currentSpeaker}: ${currentText}`);
      }

      if (speaker === 'Player' && i < conv.conversation.length - 1) {
        const nextLine = conv.conversation[i + 1];
        const nextSpeaker = Object.keys(nextLine)[0];
        const nextText = nextLine[nextSpeaker];
        if (nextSpeaker !== "Player") {
          conversationResult.add(`${nextSpeaker}: ${nextText}`);
        }
      }
    }
  }

  return Array.from(conversationResult);
}

// Event listener for search input
document.getElementById('search-input').addEventListener('input', (event) => {
  const query = event.target.value;
  if (query.length > 2) {
    search(query);
  } else {
    document.getElementById('search-results').innerHTML = '';
  }
});