<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')

async function login() {
  const form = new URLSearchParams()
  form.append('username', username.value)
  form.append('password', password.value)
  try {
    const res = await axios.post('http://localhost:8000/auth/login', form)
    localStorage.setItem('token', res.data.access_token)
    router.push('/dashboard')
  } catch (e) {
    alert('Login failed')
  }
}
</script>
