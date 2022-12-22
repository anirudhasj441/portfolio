<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <section id="banner" class="container">
      <div class="row h-100">
        <div class="col-lg-6 col-sm-6 order-md-last text-end h-100">
          <img src="../assets/banner_image.svg" class="" alt="" style="max-width: 100%;height: 100%;">
          <a href="https://storyset.com/technology" target="_blank" class="attribution">Technology illustrations by Storyset</a>
        </div>
        <div class="col-lg-6 col-sm-6 h-100">
          <div class="h-100 d-flex flex-column justify-content-center animate__animated animate__fadeInLeft">
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
      </div>
    </section>
  </main>
</template>

<style>
#banner {
  height: calc(100vh - var(--navbar-height)) !important;
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
</style>
