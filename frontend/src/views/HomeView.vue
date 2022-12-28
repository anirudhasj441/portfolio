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
            {{ bio }}
          </p>
        </div>
      </div>
    </section>
    <section id="skills" class="container pt-5">
      <h1 class="title-text text-center" style="color: var(--color-primary);font-weight: bold;">Skills</h1>
      <div class="skill-container mx-auto pb-2 px-1 rounded-3">
        <div class="row g-2 w-100 m-0">
          <div v-for="skill in skills" key="skill" class="col-md-3 col-6 p-0">
            <div class="skill mx-auto rounded-3 d-flex justify-content-evenly align-items-center">
              <img v-if="skill.icon" :src="backend.getBasePath + skill.icon" alt="">
              <h6 class="m-0">{{ skill.skill }}</h6>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="projects" class="container pt-2">
      <h1 class="title-text text-center" style="color: var(--color-primary);font-weight: bold;">My Work</h1>
      <div class="project-container mt-5">
        <div v-for="project in projects" key="project.title" class="project-row">
          <div class="project-banner">
            <img :src="backend.getBasePath + project.img" class="w-100" alt="">
          </div>
          <div class="project-detail px-3">
            <div class="project-title">
              <p class="m-0" style="color: var(--color-primary);">Feature Project</p>
              <h2 class="mb-3">{{ project.title }}</h2>
            </div>
            <div class="card-primary rounded-2">
              <p class="text-bold m-0" style="font-weight: bold;">{{ project.desc }}</p>
            </div>
            <div class="project-technologies d-flex flex-wrap mt-2">
              <span v-for="tech in project.technologies">{{ tech.name }}</span>
            </div>
            <div class="project-links d-flex flex-wrap justify-content-end align-items-center mt-2">
              <a href="#" class="project-link" target="_blank" rel="noopener noreferrer">
                <i class="bi bi-github" style="font-size: 1.5rem;"></i>
              </a>
              <RouterLink class="ms-2 btn btn-sm button-primary" :to="'/project/'+project.id">Read more</RouterLink>
            </div>
          </div>
        </div>
      </div>

    </section>
  </main>
</template>

<script>
import { BackendStore } from '../stores/backend'
import {RouterLink} from 'vue-router';
export default {
  components: {
    RouterLink
  },
  data() {
    return {
      backend: BackendStore(),
      bio: "",
      skills: [],
      projects: []
    }
  },
  methods: {
    getProfile: function () {
      let url = this.backend.getBasePath + "/get_profile";
      console.log(url)
      const xhr = new XMLHttpRequest();
      xhr.open("get", url);
      xhr.onload = () => {
        let response = JSON.parse(xhr.response);
        let data = response.data;
        this.bio = data.bio;
        this.skills = data.skills;
      }
      xhr.send();
    },
    getProjects: function () {
      let url = this.backend.getBasePath + "/get_projects";
      const xhr = new XMLHttpRequest();
      xhr.open("get", url);
      xhr.onload = () => {
        let response = JSON.parse(xhr.response);
        this.projects = response.data
        console.log(response);
      }
      xhr.send();
    }
  },
  mounted() {
    this.getProfile();
    this.getProjects();
  }
}
</script>

<style>
.full-height {
  min-height: calc(100vh - var(--navbar-height)) !important;

}

#skills {
  height: calc(100vh - var(--navbar-height)) !important;
}

#projects {
  height: calc(100vh - var(--navbar-height)) !important;

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
  margin-right: 0.3rem;
}

.skill h4 {
  font-family: 'Secular One', sans-serif;
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
}

.card-primary {
  background-color: var(--color-primary) !important;
  color: var(--vt-c-black-soft);
  padding: 1rem;
  max-width: 100%;
  /* max-height: 40%;
  overflow-y: hidden; */
}

.project-row {
  display: flex;
  justify-content: space-between;
}

.project-banner {
  width: 60%;
  background-color: var(--color-background-mute);
  opacity: 0.2;
  transition: opacity 0.5s ease-in-out;
}

.project-banner:hover {
  /* background-color: red; */
  opacity: 0.8;
}

.project-detail {
  position: absolute;
  /* flex-grow: 1; */
  width: 60%;
  /* height: 100%; */
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  z-index: 99;
  /* display: flex;
  flex-direction: column;
  justify-content: center; */
}

.project-detail .project-title {
  text-align: end;
}

.project-technologies span {
  margin-right: 1rem;
}

@media (max-width: 576px) {
  .project-banner {
    width: 100%;
  }
  .project-banner img {
    height: 100% !important;
  }

  .card-primary {
    background-color: transparent !important;
    color: var(--color-text);
    padding: 0 !important;
  }

  .project-detail {
    width: 100%;
  }

  .project-detail .project-title {
    text-align: start;
  }
}
.project-link {
  color: var(--color-border-hover);
  transition: color 0.2s ease-in-out;
}
.project-link:hover {
  color: var(--color-primary);
}
.button-primary {
  background-color: var(--color-background-mute) !important;
  font-weight: bold !important;
  color: var(--color-text) !important;
}
.button-primary:hover {
  background-color: var(--color-primary) !important;
  color: var(--vt-c-black-soft) !important;
}
</style>
