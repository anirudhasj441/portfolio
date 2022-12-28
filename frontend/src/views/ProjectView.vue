<template>
    <section id="banner" class="container pt-5">
        <div class="row">
            <div class="col-lg-4 col-md-6 col-sm-12">
                <img :src="backend.getBasePath + project.img" class="banner-img" alt="">
                <div class="project-details">
                    <h3 class="title-text m-0">{{ project.title }}</h3>
                    <p class="m-0 text-end">{{ project.start_date }} to {{ project.is_present ? 'Present' : project.end_date }}</p>
                </div>
            </div>
            <div class="col-lg-8 col-md-6 col-sm-12">
                <p>{{ project.desc }}</p>
            </div>
        </div>
    </section>
    <section id="description" class="container mt-5">
    </section>
</template>

<script>
import { BackendStore } from '../stores/backend';
export default{
    data() {
        return {
            backend: BackendStore(),
            project: {}
        }
    },
    methods: {
        getProject: function(id){
            let url = this.backend.getBasePath + '/get_project/';
            let data = {
                "id": id
            }
            const xhr = new XMLHttpRequest();
            xhr.open("post", url);
            xhr.onload = () => {
                let response = JSON.parse(xhr.response);
                this.project = response.data
                console.log(response)
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
    opacity: 0.2;
}
/* #banner { */
    /* height: calc(100vh - var(--navbar-height)) !important; */
/* } */

#banner .project-details{
    position: absolute;
    right: 1.5rem;
    bottom: 0;
}

#banner p {
    font-weight: bold;
}
.title-text{
    font-family: 'Secular One', sans-serif !important;
    color: var(--color-primary);
    text-align: end;
}
</style>