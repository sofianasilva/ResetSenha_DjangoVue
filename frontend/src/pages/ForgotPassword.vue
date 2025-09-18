<template>
  <div>
    <h2>Recuperar Senha</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="email">E-mail:</label>
        <input type="email" v-model="email" required />
      </div>
      <button type="submit" :disabled="loading">Enviar Link de Recuperação</button>
    </form>
    <p v-if="message" :class="{ error: isError }">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      loading: false,
      message: "",
      isError: false
    };
  },
  methods: {
    async submitForm() {
      this.loading = true;
      this.message = "";
      try {
        await axios.post(
          "http://localhost:8000/api/password_reset/",
          { email: this.email },
          { headers: { "Content-Type": "application/json" } }
        );
        this.message = "Link de recuperação enviado para seu e-mail.";
      } catch (error) {
        if (error.response) {
          console.error("Erro no backend:", error.response.data);
          this.message = "Erro: " + JSON.stringify(error.response.data);
        } else {
          this.message = "Erro ao enviar o link de recuperação.";
        }
      } finally {
        this.loading = false;
      }
    }
  },
};
</script>
