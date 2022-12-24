import { defineStore } from 'pinia'

export const BackendStore = defineStore('backend', {
    state: () => {
        return {base_path: "http://portfolio-api.localhost"}
    },
    getters: {
        getBasePath: (state) => {
            return state.base_path;
        }
    }
})