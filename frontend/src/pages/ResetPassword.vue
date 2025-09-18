<template>
  <div>
    <h2>Definir nova senha</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="password">Nova senha:</label>
        <input type="password" v-model="password" required />
      </div>

      <div>
        <label for="confirmPassword">Confirmar senha:</label>
        <input type="password" v-model="confirmPassword" required />
      </div>

      <button type="submit" :disabled="loading">Alterar senha</button>
    </form>

    <p v-if="message" :class="{ error: isError }">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      password: "",
      confirmPassword: "",
      loading: false,
      message: "",
      isError: false,
    }
  },
  computed: {
    token() {
      return this.$route.params.token
    },
  },
  methods: {
    async submitForm() {
      if (this.password !== this.confirmPassword) {
        this.message = "As senhas não coincidem!"
        this.isError = true
        return
      }

      this.loading = true
      this.message = ""
      try {
        await axios.post(
          "http://localhost:8000/api/password_reset/confirm/",
          {
            token: this.token,
            password: this.password,
          },
          { headers: { "Content-Type": "application/json" } }
        )
        this.message = "Senha redefinida com sucesso!"
        this.isError = false
      } catch (error) {
        if (error.response) {
          this.message = "Erro: " + JSON.stringify(error.response.data)
        } else {
          this.message = "Erro ao redefinir a senha."
        }
        this.isError = true
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style>
.error {
  color: red;
}
</style>
