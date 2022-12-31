<template>
    <section id="banner" class="container pt-3">
        <div class="project-details">
            <h3 class="title-text text-center m-0">{{ project.title }}</h3>
        </div>
        <div class="row g-3">
            <div class="col-lg-4 col-md-6 col-sm-12">
                <img :src="backend.getBasePath + project.img" class="banner-img" alt="">
            </div>
            <div class="col-lg-8 col-md-6 col-sm-12">
                <p>{{ project.desc }}</p>
            </div>
            <div class="d-flex justify-content-end align-items-center flex-wrap">
                <div v-for="tech in project.technologies" class="ms-3" style="font-weight: bold;">{{ tech.name }}</div>
            </div>
            <div class="d-flex justify-content-end align-items-center">
                <p class="m-0 text-end">{{ project.start_date }} to {{ project.is_present ? 'Present' : project.end_date
}}
                </p>
                <a v-if="project.git_repo" :href="project.git_repo" class="ms-2 project-link" target="_blank"
                    rel="noopener noreferrer">
                    <i class="bi bi-github" style="font-size: 1.5rem;"></i>
                </a>
            </div>
        </div>
    </section>
    <section v-if="project.screenshots.length > 0" id="screenshots" class="container my-5">
        <h1 class="title-text text-center">Screenshots</h1>
        <div class="row g-3">
            <div v-for="img in project.screenshots" class="col-lg-4 col-md-4 col-sm-12">
                <img class="img-fluid" :src="backend.getBasePath + img.img" alt="">
            </div>
        </div>
    </section>
    <footer>
        <Footer></Footer>
    </footer>
</template>

<script>
import { BackendStore } from '../stores/backend';
import Footer from '../components/Footer.vue';
export default {
    components: {
        Footer
    },
    data() {
        return {
            backend: BackendStore(),
            project: {
                screenshots: []
            }
        }
    },
    methods: {
        getProject: function (id) {
            let url = this.backend.getBasePath + '/get_project/';
            let data = {
                "id": id
            }
            const xhr = new XMLHttpRequest();
            xhr.open("post", url);
            xhr.onload = () => {
                let response = JSON.parse(xhr.response);
                this.project = response.data;
            }
            xhr.send(JSON.stringify(data))
        }
    },
    mounted() {
        this.getProject(this.$route.params.id);
    }
}
</script>
<style scoped>
.banner-img {
    /* max-height: 50vh; */
    width: 100%;
    background-color: var(--color-background);
    /* opacity: 0.2; */
}

/* #banner { */
/* height: calc(100vh - var(--navbar-height)) !important; */
/* } */

/* #banner .project-details{ */
/* position: absolute;
    right: 1.5rem;
    bottom: 0; */
/* } */

#banner p {
    font-weight: bold;
}

.title-text {
    font-family: 'Secular One', sans-serif !important;
    color: var(--color-primary);
    text-align: end;
}
</style>