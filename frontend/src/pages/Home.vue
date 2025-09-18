<script>
import { useAuthStore } from '../store/auth.js'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()

    return {
      authStore,
      router
    }
  },
  methods: {
    async logout() {
      try {
        await this.authStore.logout(this.$router)
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted() {
    await this.authStore.fetchUser()
  }
}
</script>

<template>
  <h1>Bem vinda a página inicial do Zeppelin</h1>

  <div v-if="authStore.isAuthenticated">
    <p>Oi! {{ authStore.user?.username }}!</p>
    <p>Você tá logado.</p>
    <button @click="logout">Logout</button>
  </div>

  <p v-else>
    Faz o <router-link to="/login">Login</router-link> ai fio
    
    <br>
    Ah, caso não tenha login crie um
    <router-link to="/register">Registro</router-link>
    </br>
  </p>
</template>

