<template>
    <main>
        <div class="h-100">
            <iframe v-if="resume != ''" :src="backend.getBasePath + resume" class="w-100"></iframe>
        </div>
    </main>
</template>
<script>
// import pdf from 'vue-pdf';
import { BackendStore } from '../stores/backend';
export default {
    components: {
        // pdf
    },
    data() {
        return {
            backend: BackendStore(),
            resume: ""
        }
    },
    methods: {
        getProfile: function () {
            let url = this.backend.getBasePath + '/get_profile/';
            const xhr = new XMLHttpRequest();
            xhr.open("get", url);
            xhr.onload = () => {
                let response = JSON.parse(xhr.response);
                let data = response.data;
                this.resume = data.resume;
                console.log(this.resume)
            }
            xhr.send();
        },
    },
    mounted() {
        console.log("Hello");
        this.getProfile();
    }
}
</script>
<style scoped>
div {
    height: calc(100vh - var(--navbar-height)) !important;
    width: 100%;
}
main iframe {
    display: block;
    height: 100%;
}
</style>