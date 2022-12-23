<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <section id="banner" class="container">
      <div class="row h-100">
        <div class="full-height col-lg-6 col-sm-6 order-md-last text-end">
          <img src="../assets/banner_image.svg" class="" alt="" style="max-width: 100%;height: 100%;">
          <a href="https://storyset.com/technology" target="_blank" class="attribution">Technology illustrations by
            Storyset</a>
        </div>
        <div
          class="full-height d-flex flex-column justify-content-center animate__animated animate__fadeInLeft col-lg-6 col-sm-6 h-100">
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
    <section id="skills" class="container pt-5">
      <!-- <div style="position: relative;"> -->
      <h1 class="title-text text-center" style="color: var(--color-primary);font-weight: bold;">Skills</h1>
      <div class="skill-container mx-auto pb-2 px-1 rounded-3">
        <div class="row g-2 w-100 m-0">
          <div v-for="i in 8" key="i" class="col-md-3 col-6 p-0">
            <div class="skill mx-auto rounded-3 d-flex justify-content-evenly align-items-center">
              <img src="../assets/logo.svg" alt="">
              <h6 class="m-0">Vue JS</h6>
            </div>
          </div>
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

.skill img {
  width: 1.5rem;
  /* height: 60%; */
  margin-right: 0.3rem;
}

.skill h4 {
  font-family: 'Secular One', sans-serif;
  ;
  /* color: var(--color-primary); */
}

.skill {
  width: 95%;
  padding: 0.8rem;
  background-color: var(--color-background);
  display: flex;
  color: white;
}

.skill-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 95%;
  max-width: 600px;
  flex-wrap: wrap;
  background-color: var(--color-primary);
  /* opacity: 0.5; */
}
</style>
