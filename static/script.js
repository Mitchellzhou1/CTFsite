allEdSheeranSongs = [
    {
        title: "Shape of You",
        img: "JGwWNGJdvx8",
        popularityRank: 1,
        youtubeLink: "https://www.youtube.com/watch?v=JGwWNGJdvx8"
    },
    {
        title: "Thinking Out Loud",
        img: "lp-EO5I60KA",
        popularityRank: 2,
        youtubeLink: "https://www.youtube.com/watch?v=lp-EO5I60KA"
    },
    {
        title: "Photograph",
        img: "nSDgHBxUbVQ",
        popularityRank: 3,
        youtubeLink: "https://www.youtube.com/watch?v=nSDgHBxUbVQ"
    },
    {
        title: "Castle on the Hill",
        img: "K0ibBPhiaG0",
        popularityRank: 4,
        youtubeLink: "https://www.youtube.com/watch?v=K0ibBPhiaG0"
    },
    {
        title: "Galway Girl",
        img: "87gWaABqGYs",
        popularityRank: 5,
        youtubeLink: "https://www.youtube.com/watch?v=87gWaABqGYs"
    },
    {
        title: "Perfect",
        img: "2Vv-BfVoq4g",
        popularityRank: 6,
        youtubeLink: "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    },
    {
        title: "I See Fire",
        img: "2fngvQS_PmQ",
        popularityRank: 7,
        youtubeLink: "https://www.youtube.com/watch?v=2fngvQS_PmQ"
    },
    {
        title: "Bloodstream",
        img: "XIJHg1XWR7o",
        popularityRank: 8,
        youtubeLink: "https://www.youtube.com/watch?v=XIJHg1XWR7o"
    },
    {
        title: "Dive",
        img: "Wv2rLZmbPMA",
        popularityRank: 9,
        youtubeLink: "https://www.youtube.com/watch?v=Wv2rLZmbPMA"
    },
    {
        title: "Happier",
        img: "m7Bc3pLyij0",
        popularityRank: 10,
        youtubeLink: "https://www.youtube.com/watch?v=m7Bc3pLyij0"
    },
    {
        title: "The A Team",
        img: "UAWcs5H-qgQ",
        popularityRank: 11,
        youtubeLink: "https://www.youtube.com/watch?v=UAWcs5H-qgQ"
    },
    {
        title: "You Need Me, I Don't Need You",
        img: "ZXvzzTICvJs",
        popularityRank: 12,
        youtubeLink: "https://www.youtube.com/watch?v=ZXvzzTICvJs"
    },
    {
        title: "Sing",
        img: "tlYcUqEPN58",
        popularityRank: 13,
        youtubeLink: "https://www.youtube.com/watch?v=tlYcUqEPN58"
    },
    {
        title: "Give Me Love",
        img: "FOjdXSrtUxA",
        popularityRank: 14,
        youtubeLink: "https://www.youtube.com/watch?v=FOjdXSrtUxA"
    },
    {
        title: "One",
        img: "Ix9NXVIbm2A",
        popularityRank: 15,
        youtubeLink: "https://www.youtube.com/watch?v=Ix9NXVIbm2A"
    }
];

function createEdSheeranSongElement(song) {
    let songElement = document.createElement("DIV");
    songElement.style.backgroundColor = "#fff";
    songElement.classList.add('song');

    let songTitle = document.createElement("H2");
    songTitle.classList.add('songTitle');
    songTitle.innerText = song['title'];
    songElement.appendChild(songTitle);

    let coverIMG = document.createElement("IMG");
    coverIMG.src = `/images/${song.title}.jpg`;
    songElement.appendChild(coverIMG);

    let youtubeLink = document.createElement("A");
    youtubeLink.classList.add('youtubeLink');
    youtubeLink.href = song['youtubeLink'];
    youtubeLink.target = "_blank";
    youtubeLink.innerText = "Watch on YouTube";
    songElement.appendChild(youtubeLink);

    let popularityRank = document.createElement("P");
    popularityRank.classList.add('popularityRank');
    popularityRank.innerText = "Popularity Rank: " + song['popularityRank'];
    songElement.appendChild(popularityRank);

    songsSection.appendChild(songElement);
}

const songsSection = document.getElementById("songs");

allEdSheeranSongs.forEach(song => {
    createEdSheeranSongElement(song);
});


document.addEventListener("DOMContentLoaded", function() {
    const loginButton = document.getElementById("loginButton");

    // Redirect to the login route when the button is clicked
    loginButton.addEventListener("click", function() {
        // Redirect to the login route handled by Flask
        window.location.href = "/login";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const loginButton = document.getElementById("logOut");

    // Redirect to the login route when the button is clicked
    loginButton.addEventListener("click", function() {
        // Redirect to the login route handled by Flask
        window.location.href = "/logout";
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const loginButton = document.getElementById("Chat");

    // Redirect to the login route when the button is clicked
    loginButton.addEventListener("click", function() {
        // Redirect to the login route handled by Flask
        window.location.href = "/chat";
    });
});
