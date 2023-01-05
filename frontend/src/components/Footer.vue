<template>
    <main class="container py-3 text-center">
        <h6 class="text-center m-0">Design & Developed By Anirudha Jadhav</h6>
        <a class="contact-link" :href="github_link" target="_blank">
            <i class="bi bi-github" style="font-size: 1.5rem;"></i>
        </a>
    </main>
</template>

<script>
import { BackendStore } from '../stores/backend'
export default {
    data() {
        return {
            backend: BackendStore(),
            github_link: ''
        }
    },
    methods: {
        getLink: function() {
            let url = this.backend.getBasePath + '/get_profile';
            const xhr = new XMLHttpRequest();
            xhr.open("get", url);
            xhr.onload = () => {
                let response = JSON.parse(xhr.response);
                let contacts = response.data.contacts[0];
                this.github_link = contacts.github;

            }
            xhr.send()
        }
    },
    mounted() {
        this.getLink();
    }
}
</script>