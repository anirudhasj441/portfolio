<template>
    <nav class="nav-bar">
        <div class="container-fluid h-100 d-flex align-items-center justify-content-between">
            <div class="brand">
                Portfolio
            </div>
            <button v-if="nav_collapse" id="navbar-toggle" class="btn p-0 shadow-none border-0" @click="show_nav=!show_nav"><i class="bi" :class="show_nav ? 'bi-x' : 'bi-list'" style="font-size: 2rem;"></i></button>
            <ul class="nav-menu h-100 p-0" :style="nav_style" @blur="blurNavBar">
                <li class="px-3"><RouterLink to="/">Home</RouterLink></li>
                <li class="px-3"><RouterLink to="/about">About</RouterLink></li>
            </ul>
        </div>
    </nav>
</template>
<script>
import { RouterLink } from 'vue-router';
export default{
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
        blurNavBar: function(){
            console.log("blurrrr")
            let width = window.innerWidth;
            if(width <= 576){
                this.show_nav = false;
            }
        }
    },
    mounted() {
        let width = window.innerWidth;
        this.nav_collapse = width <= 576 ? true : false;
        window.addEventListener("resize", (e)=>{
            let width = window.innerWidth;
            this.nav_collapse = width <= 576 ? true : false;
            this.nav_style = width <= 576 ? {width: '0'} : {};
            if(width <= 576){
                this.show_nav = false;
            }
        })
    },
    watch: {
        show_nav(value){
            console.log("changed: ", value)
            this.nav_style = value ? {width: '75vw'} : {width: '0'};
        }
    }
}
</script>
<style scoped>
.nav-bar{
    position: sticky;
    top: 0;
    height: var(--navbar-height);
    background-color: var(--color-background-mute);
    z-index: 999;
}
.nav-menu{
    /* position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%); */
    display: flex;
    align-items: center;
    list-style: none;
    margin-bottom: 0 !important;
}

.nav-menu li{
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    /* margin-left: 1rem; */
}

.nav-menu a.router-link-exact-active{
    color: var(--bs-primary);
}

@media (min-width: 576px){
    .nav-menu li:has(a.router-link-exact-active)::after {
        content: '';
        width: 100%;
        height: 10%;
        background-color: var(--bs-primary);
        position: absolute;
        bottom: 0;
    }
}



.nav-menu a{
    color: var(--color-text);
    text-decoration: none;
}

/* brekpoint for sm */
@media (max-width: 576px) {
    .nav-menu{
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
    .nav-menu li{
        width: 100%;
        height: var(--navbar-height) !important;
    }

    /* .nav-menu li a.router-link-exact-active{
        color: var(--bs-primary);
    } */

    #navbar-toggle{
        /* display: block; */
        color: var(--color-text);
        position: absolute;
        top: 50%;
        right: 0;
        transform: translateY(-50%);
        z-index: 9999;
    }
}
</style>