<template>
  <div>
    <h1>Dashboard</h1>
    <p v-if="user">Welcome, {{ user.username }} ({{ user.role }})</p>
    <div>
      <h2>Your Goals</h2>
      <ul>
        <li v-for="g in goals" :key="g.id">{{ g.title }} - {{ g.description }}</li>
      </ul>
      <form @submit.prevent="addGoal">
        <input v-model="title" placeholder="Title" />
        <input v-model="description" placeholder="Description" />
        <button type="submit">Add Goal</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const user = ref(null)
const goals = ref([])
const title = ref('')
const description = ref('')

const api = axios.create({ baseURL: 'http://localhost:8000' })
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

async function fetchData() {
  const me = await api.get('/users/me')
  user.value = me.data
  const g = await api.get('/goals/')
  goals.value = g.data
}

async function addGoal() {
  const g = await api.post('/goals/', { title: title.value, description: description.value })
  goals.value.push(g.data)
  title.value = ''
  description.value = ''
}

onMounted(fetchData)
</script>
