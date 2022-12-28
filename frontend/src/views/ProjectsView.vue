<template>
  <div class="container">
    <div v-for="project, key in projects" key="project.title" class="project-row mb-5"
      :class="(key + 1) % 2 == 0 ? 'inverted' : ''">
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
          <a v-if="project.git_repo" :href="project.git_repo" class="me-2 project-link" target="_blank"
            rel="noopener noreferrer">
            <i class="bi bi-github" style="font-size: 1.5rem;"></i>
          </a>
          <RouterLink class="btn btn-sm button-secondary" :to="'/project/' + project.id">Read more</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { BackendStore } from '../stores/backend'
import { RouterLink } from 'vue-router';
export default {
  components: {
    RouterLink
  },
  data() {
    return {
      backend: BackendStore(),
      projects: []
    }
  },
  methods: {
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
    this.getProjects();
  }
}
</script>

<style>
/* @media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
} */
</style>
