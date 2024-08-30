const mario = document.getElementById('mario');
        const pipe = document.getElementById('pipe');
        const successModal = document.getElementById('successModal');
        const gameOverModal = document.getElementById('gameOverModal');
        const successButton = document.getElementById('successButton');
        const retryButton = document.getElementById('retryButton');

        let jumpCount = 0;

        function jump() {
            if (!mario.classList.contains('jump')) {
                mario.classList.add('jump');
                setTimeout(() => {
                    mario.classList.remove('jump');
                }, 500);
                jumpCount++;
                if (jumpCount >= 8) {
                    successModal.style.display = 'flex';
                    clearInterval(checkCollision);
                }
            }
        }

        document.addEventListener('keydown', function (event) {
            if (event.code === 'Space') {
                jump();
            }
        });

        document.addEventListener('touchstart', function () {
            jump();
        });

        const checkCollision = setInterval(() => {
            const marioBottom = parseInt(window.getComputedStyle(mario).getPropertyValue('bottom'));
            const pipeLeft = parseInt(window.getComputedStyle(pipe).getPropertyValue('left'));

            if (pipeLeft > 0 && pipeLeft < 80 && marioBottom <= 30) {
                pipe.style.animation = 'none';
                pipe.style.left = `${pipeLeft}px`;
                gameOverModal.style.display = 'flex';
                clearInterval(checkCollision);
            }
        }, 10);

        successButton.addEventListener('click', () => {
            window.location.href = '{% url "premio" %}';
        });

        retryButton.addEventListener('click', () => {
            window.location.reload();
        });
