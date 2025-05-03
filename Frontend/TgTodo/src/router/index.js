import {createRouter, creteWebHistory} from 'vue-router'
import TasksView from '../views/TaskView.vue'
import ProfileView from '..views/ProfileView.vue'

const routes = [
    {
        path: '/',
        name: 'Tasks',
        component: TasksView
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView
    }
]

const router = createRouter({
    history: creteWebHistory(import.meta.env.BASE_URL),
    routes
})