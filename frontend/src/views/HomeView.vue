<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <section id="banner" class="container">
      <div class="row h-100">
        <div class="full-height col-lg-6 col-sm-6 order-md-last text-end">
          <img src="../assets/banner_image.svg" class="" alt="" style="max-width: 100%;height: 100%;">
          <a href="https://storyset.com/technology" target="_blank" class="attribution">Technology illustrations by Storyset</a>
        </div>
        <div class="full-height d-flex flex-column justify-content-center animate__animated animate__fadeInLeft col-lg-6 col-sm-6 h-100">
          <p class="m-0" style="font-size: 1rem;">Hello I am, </p>
          <h1 class="title-text" style="color: var(--color-primary);">Anirudha Jadhav</h1>
          <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempora nulla quis fugiat. Reprehenderit
            suscipit fugit perferendis iusto nobis cum necessitatibus ut facere vel totam, illum quidem earum
            voluptatibus eius quasi eligendi pariatur sapiente explicabo dolores, facilis aperiam, nesciunt beatae
            corporis ea. Libero, eaque dolorum reprehenderit quod, eligendi ad, molestias minus aliquam beatae
            assumenda perspiciatis a quas totam! Soluta adipisci ipsam animi quibusdam, vel deleniti perspiciatis
            atque assumenda suscipit illum sunt beatae quam incidunt reprehenderit ullam? Dicta, facilis distinctio,
            odit animi consequatur eveniet culpa provident obcaecati porro fuga, sunt voluptatum optio.
          </p>
        </div>
      </div>
    </section>
    <section id="skills" class="container p-5">
      <!-- <div style="position: relative;"> -->
        <h1 class="title-text text-center" style="color: var(--color-primary);font-weight: bold;">Skills</h1>
        <div class="skill-container row gx-3 p-3 rounded">
          <div class="col skill rounded">
            <img src="../assets/logo.svg" alt="">
            <h4 class="m-0">Vue JS</h4>
          </div>
          <div class="col skill rounded">
            <img src="../assets/logo.svg" alt="">
            <h4 class="m-0">Vue JS</h4>
          </div>
          <div class="col skill rounded">
            <img src="../assets/logo.svg" alt="">
            <h4 class="m-0">Vue JS</h4>
          </div>
          <div class="col skill rounded">
            <img src="../assets/logo.svg" alt="">
            <h4 class="m-0">Vue JS</h4>
          </div>
        </div>
      <!-- </div> -->
    </section>
  </main>
</template>

<style>
.full-height {
  min-height: calc(100vh - var(--navbar-height)) !important;

}
/* #banner {
  margin-top: var(--navbar-height) !important;
} */

#skills {
  height: calc(100vh - var(--navbar-height)) !important;
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  /* margin-top: var(--navbar-height) !important; */
}

.attribution {
  position: absolute;
  bottom: 0;
  right: 0;
  font-size: 0.75rem;
  text-decoration: none;
  color: var(--color-primary);
}

.attribution:hover {
  color: var(--color-primary);
}

.title-text {
  font-size: 3.5rem;
  font-family: 'Secular One', sans-serif;
}
.skill img{
  width: 30px;
  /* height: 60%; */
  margin-right: 0.3rem;
}
.skill h4{
  font-family: 'Secular One', sans-serif;;
  /* color: var(--color-primary); */
}
.skill{
  /* height: 100px;
  width: 100px; */
  /* width: max-content; */
  padding: 0.8rem;
  margin: 0 0.5rem;
  background-color: var(--color-background-mute);
  display: flex;
  /* flex-direction: column; */
  /* justify-content: space-evenly; */
  /*align-items: center; */
}
.skill-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* mwidth: 90vw !important; */
  flex-wrap: wrap;
  background-color: var(--color-border-hover);
}
@media(max-width: 576px) {
  .skill-container .skill {
    margin-top: 1rem !important;
  }
  /* .skill-container:first-child {
    margin-top: 0 !;
  } */
}
</style>
