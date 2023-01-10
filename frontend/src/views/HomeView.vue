<template>
  <main>
    <section id="banner" class="container">
      <div class="row h-100">
        <div class="full-height col-lg-6 col-sm-6 order-md-last text-end">
          <img src="../assets/banner_image.svg" class="animate__animated animate__fadeInRight" alt="" style="max-width: 100%;height: 100%;">
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
            <div class="skill mx-auto rounded-3 d-flex justify-content-between align-items-center">
              <img v-if="skill.icon" :src="backend.getBasePath + skill.icon" alt="">
              <div class="text-center flex-grow-1">
                <h6 class="m-0 text-center">{{ skill.skill }}</h6>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="projects" class="container py-3">
      <h1 class="title-text text-center" style="color: var(--color-primary);font-weight: bold;">My Work</h1>
      <div class="project-container mt-5">
        <div v-for="project, key in projects.slice(0,2)" key="project.title" class="project-row mb-5"
          :class="(key + 1) % 2 == 0 ? 'inverted' : ''">
          <div class="project-banner">
            <img :src="backend.getBasePath + project.img" class="w-100" alt="">
          </div>
          <div class="project-detail px-3">
            <div class="project-title">
              <p class="m-0" >Feature Project</p>
              <h2 class="mb-3" style="color: var(--color-primary);">{{ project.title }}</h2>
            </div>
            <div class="card-primary rounded-2">
              <p class="text-bold m-0" style="font-weight: bold;">{{ project.desc }}</p>
            </div>
            <div class="project-technologies d-flex flex-wrap mt-2">
              <span v-for="tech in project.technologies">{{ tech.name }}</span>
            </div>
            <div class="project-links d-flex flex-wrap justify-content-end align-items-center mt-2">
              <a v-if="project.git_repo" :href="project.git_repo" class="me-2 project-link" target="_blank"
                rel="noopener noreferrer">
                <i class="bi bi-github" style="font-size: 1.5rem;"></i>
              </a>
              <RouterLink class="btn btn-sm button-secondary" :to="'/project/' + project.id">Read more</RouterLink>
            </div>
          </div>
        </div>
      </div>
      <div class="text-center">
        <RouterLink class="button-primary btn btn-primary" to="/projects">ALL PROJECTS</RouterLink>
      </div>
    </section>
    <section id="contact" class="container py-3">
      <h1 class="title-text text-center" style="color: var(--color-primary);">Contact Me</h1>
      <div class="contacts-row">
        <div v-if="contact.whatsapp_no" class="me-4">
          <a class="contact-link" :href="'https://wa.me/'+contact.whatsapp_no" target="_blank">
            <i class="bi bi-whatsapp" style="font-size: 3rem;"></i>
          </a>
        </div>
        <div v-if="contact.email" class="me-4">
          <a class="contact-link" :href="'mailto:' + contact.email" target="_blank">
            <i class="bi bi-envelope-at" style="font-size: 3rem;"></i>
          </a>
        </div>
        <div v-if="contact.linkedin" class="me-4">
          <a class="contact-link" :href="contact.linkedin" target="_blank">
            <i class="bi bi-linkedin" style="font-size: 3rem;"></i>
          </a>
        </div>
        <div v-if="contact.insta" class="me-4">
          <a class="contact-link" :href="contact.insta" target="_blank">
            <i class="bi bi-instagram" style="font-size: 3rem;"></i>
          </a>
        </div>
      </div>
    </section>
  </main>
  <footer>
    <Footer></Footer>
  </footer>
</template>

<script>
import { BackendStore } from '../stores/backend'
import { RouterLink } from 'vue-router';
import Footer from '../components/Footer.vue';
export default {
  components: {
    RouterLink,
    Footer
  },
  data() {
    return {
      loading: true,
      backend: BackendStore(),
      bio: "",
      skills: [],
      projects: [],
      contact: {}
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
        this.contact = data.contacts[0];
        this.loading = false;
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
  min-height: calc(100vh - var(--navbar-height)) !important;
  
}
#contact {
  min-height: calc(100vh - var(--navbar-height)) !important;
}

footer { 
  background-color: var(--color-background-mute);
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

.skill img {
  width: 1.5rem;
  aspect-ratio: 1 / 1;
  margin-right: 0.3rem;
}

.skill h4 {
  font-family: 'Secular One', sans-serif;
}

.skill {
  width: 95%;
  padding: 0.8rem;
  background-color: var(--color-background);
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  color: white;
}

.skill-container {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
      -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  width: 95%;
  max-width: 600px;
  -ms-flex-wrap: wrap;
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
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
}

.project-banner {
  width: 60%;
  background-color: var(--color-background-mute);
  opacity: 0.2;
  -webkit-transition: opacity 0.5s ease-in-out;
  -o-transition: opacity 0.5s ease-in-out;
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
  -webkit-transform: translateY(-50%);
      -ms-transform: translateY(-50%);
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

.project-row.inverted {
  -webkit-box-orient: horizontal !important;
  -webkit-box-direction: reverse !important;
      -ms-flex-direction: row-reverse !important;
          flex-direction: row-reverse !important;
}

.project-row.inverted .project-detail {
  position: absolute;
  /* flex-grow: 1; */
  width: 60%;
  /* height: 100%; */
  left: 0 !important;
  top: 50%;
  -webkit-transform: translateY(-50%);
      -ms-transform: translateY(-50%);
          transform: translateY(-50%);
  z-index: 99;
  /* display: flex;
  flex-direction: column;
  justify-content: center; */
}

.project-row.inverted .project-detail .project-title {
  text-align: start;
}

.project-row.inverted .project-links {
  -webkit-box-pack: start !important;
      -ms-flex-pack: start !important;
          justify-content: start !important;
}

.contacts-row {
  display: flex;
  flex-wrap: wrap !important;
  width: max-content !important;
  position: absolute !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* transform: translateX(-50%); */
}

.contact-link {
  color: var(--color-primary);
}

.contact-link:hover i {
  color: var(--color-primary);
  text-shadow: 0 0 5px var(--color-primary) !important;
}

@media (max-width: 576px) {
  .project-banner {
    height: 100%;
    width: 100%;
    /* display: none; */
    position: absolute;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }

  .project-row.inverted .project-links {
    -webkit-box-pack: end !important;
        -ms-flex-pack: end !important;
            justify-content: end !important;
  }

  .card-primary {
    background-color: transparent !important;
    color: var(--color-text);
    padding: 0 !important;
  }

  .project-detail,
  .project-row.inverted .project-detail {
    width: 100%;
    height: 100% !important;
    position: relative;
    -webkit-transform: translateY(0);
        -ms-transform: translateY(0);
            transform: translateY(0);
  }

  .project-detail .project-title {
    text-align: start;
  }

  .contacts-row {
    flex-direction: column !important;
  }
}

.project-link {
  color: var(--color-border-hover);
  -webkit-transition: color 0.2s ease-in-out;
  -o-transition: color 0.2s ease-in-out;
  transition: color 0.2s ease-in-out;
}

.project-link:hover {
  color: var(--color-primary);
}

.button-primary {
  background-color: var(--color-primary) !important;
  color: var(--bs-dark) !important;
  font-weight: bold !important;
}

.button-primary:hover {
  -webkit-box-shadow: 0 0 10px var(--color-primary) !important;
          box-shadow: 0 0 10px var(--color-primary) !important;
}

.button-secondary {
  background-color: var(--color-background-mute) !important;
  font-weight: bold !important;
  color: var(--color-text) !important;
}

.button-secondary:hover {
  background-color: var(--color-primary) !important;
  color: var(--vt-c-black-soft) !important;
  -webkit-box-shadow: 0 0 10px var(--color-primary) !important;
          box-shadow: 0 0 10px var(--color-primary) !important;
}
</style>
