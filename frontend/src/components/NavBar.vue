<template>
    <div class="nav-bar">
        <div class="container-fluid h-100 d-flex align-items-center justify-content-between">
            <div class="brand d-flex align-items-center">
                <RouterLink to="/">
                    <img src="../assets/programmer.png" alt="logo" style="width: 3rem;">
                </RouterLink>
                <!-- <h5 class="my-0 ms-2">
                    Anirudha Jadhav
                </h5> -->
            </div>
            <div v-if="nav_collapse" class="toggle-btn" :class="show_nav ? 'open' : ''" @click="show_nav = !show_nav">
                <div class="hamburger"></div>
            </div>
            <!-- <button v-if="nav_collapse" id="navbar-toggle" class="btn p-0 shadow-none border-0" @click="show_nav=!show_nav"><i class="bi" :class="show_nav ? 'bi-x' : 'bi-list'" style="font-size: 2rem;"></i></button> -->
            <ul class="nav-menu h-100 p-0" :style="nav_style">
                <li class="px-3">
                    <RouterLink to="/">Home</RouterLink>
                </li>
                <li class="px-3">
                    <RouterLink to="/projects">Projects</RouterLink>
                </li>
                <li class="px-3">
                    <RouterLink to="/resume">Resume</RouterLink>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
import { RouterLink } from 'vue-router';
export default {
    components: {
        RouterLink
    },
    data() {
        return {
            show_nav: false,
            nav_collapse: false,
            nav_style: {}
        }
    },
    methods: {

    },
    mounted() {
        let width = window.innerWidth;
        this.nav_collapse = width <= 576 ? true : false;
        window.addEventListener("resize", (e) => {
            let width = window.innerWidth;
            this.nav_collapse = width <= 576 ? true : false;
            this.nav_style = width <= 576 ? { width: '0' } : {};
            if (width <= 576) {
                this.show_nav = false;
            }
        })
        window.addEventListener("click", (event) => {
            const el = event.target;
            if (
                !el.classList.contains("nav-menu") &&
                el.tagName != "A" &&
                !el.classList.contains("toggle-btn") &&
                !el.classList.contains("hamburger")
            ){
                this.show_nav = false;
            }
        })
    },
    watch: {
        show_nav(value) {
            console.log("changed: ", value)
            this.nav_style = value ? { width: '75vw' } : { width: '0' };
        }
    }
}
</script>
<style scoped>
.nav-bar {
    width: 100%;
    height: var(--navbar-height);
    background-color: var(--color-background-mute);
    z-index: 999;
}

.nav-menu {
    /* position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%); */
    display: flex;
    align-items: center;
    list-style: none;
    margin-bottom: 0 !important;
}

.nav-menu li {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    /* margin-left: 1rem; */
}

.nav-menu a.router-link-exact-active {
    color: var(--color-primary);
}

@media (min-width: 576px) {
    .nav-menu li::after {
        content: '';
        left: 0;
        width: 0;
        height: 10%;
        background-color: var(--color-primary);
        position: absolute;
        bottom: 0;
        transition: width 0.3s ease-in;
    }

    .nav-menu li:has(a.router-link-exact-active)::after {
        content: '';
        width: 100%;
        height: 10%;
        left: 0;
        background-color: var(--color-primary);
        position: absolute;
        bottom: 0;
    }
}



.nav-menu a {
    color: var(--color-text);
    text-decoration: none;
    font-weight: bold;
}

/* brekpoint for sm */
@media (max-width: 576px) {
    .nav-menu {
        position: fixed;
        top: var(--navbar-height);
        right: 0 !important;
        background-color: var(--color-background-mute) !important;
        height: 100vh !important;
        display: block;
        width: 0;
        overflow: hidden;
        transition: width 0.3s ease-in-out;
    }

    .nav-menu li {
        width: 100%;
        max-height: 2.75rem !important;
    }

    .nav-menu li a {
        width: 100%;
        text-align: center;
    }

    /* .nav-menu li a.router-link-exact-active{
        color: var(--bs-primary);
    } */

    #navbar-toggle {
        /* display: block; */
        color: var(--bs-primary);
        position: absolute;
        top: 50%;
        right: 0;
        transform: translateY(-50%);
        z-index: 9999;
    }

    .toggle-btn {
        display: flex;
        justify-content: center;
        align-items: center;
        height: var(--navbar-height);
        /* background-color: blue; */
        /* border: 3px solid var(--color-text); */
        width: 2rem;
        transition: all 0.3s ease-in-out;
    }

    .hamburger {
        position: relative;
        border-radius: 20px;
        width: 100%;
        height: 8%;
        background-color: var(--color-primary);
        transition: all 0.3s ease-in-out;
    }

    .hamburger::after,
    .hamburger::before {
        content: '';
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        border-radius: 20px;
        background-color: var(--color-primary);
        position: absolute;
        transition: all 0.3s ease-in-out;
    }

    .hamburger::after {
        transform: translateY(-200%);
    }

    .hamburger::before {
        transform: translateY(200%);
    }

    .toggle-btn.open {
        transform: rotate(180deg);
    }

    .toggle-btn.open .hamburger {
        background: transparent;
        box-shadow: none;
    }

    .toggle-btn.toggle-btn.open .hamburger::after {
        transform: rotate(calc(45deg));
    }

    .toggle-btn.toggle-btn.open .hamburger::before {
        transform: rotate(-45deg);
    }

}
</style>