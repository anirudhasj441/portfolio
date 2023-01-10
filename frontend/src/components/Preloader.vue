<template>
    <div id="preloader">
        <div class="d-flex h-100 justify-content-center align-items-center">
            <div class="d-flex align-items-baseline">
                <h1 class="title-text">
                    LOADING
                </h1>
                <div class="dot-1 rounded-circle"></div>
                <div class="dot-2 rounded-circle"></div>
                <div class="dot-3 rounded-circle"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#preloader {
    width: 100%;
    height: 100vh;
    position: fixed;
    top:0;
    left:0;
    z-index: 999;
    background-color: var(--color-background);
}
h1 {
    color: var(--color-primary);
    font-family: 'Secular One', sans-serif;
}
.dot-1, .dot-2, .dot-3 { 
    margin-left: 0.5rem;
    background-color: var(--color-primary);
    width: .8rem;
    height: .8rem;
    animation: pop-up 1s infinite;
}
.dot-1 {
    animation-delay: -.24s;
}
.dot-2 {
    animation-delay: -.12s;
}

@keyframes pop-up{
    0% {
        /* transform: translateY(0); */
        opacity: 1;
    }
    100% {
        /* transform: translateY(0); */
        opacity: 0;
    }
}
</style>