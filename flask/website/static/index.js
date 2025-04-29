function toggleGames() {
    const moreGames = document.querySelector('.more-games');
    const btn = document.querySelector('.see-more-btn');
    
    // Toggle visibility of the additional games
    moreGames.classList.toggle('open');
  
    // Change the button text depending on the visibility of the games
    if (moreGames.classList.contains('open')) {
      btn.textContent = "See Less";
    } else {
      btn.textContent = "See More";
    }
  
    
    // Move the "See More" button to the very bottom of the page after it's clicked
    const gameList = document.getElementById('game-list');
    const seeMoreBtn = document.getElementById('see-more-btn');
    
    gameList.appendChild(seeMoreBtn); // Moves it to the end of the list every time
  }    