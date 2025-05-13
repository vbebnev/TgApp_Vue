<template>
    <div class="profile-container">
        <h2>Profile</h2>
        <div class="profile-info">
            <p><strong>ID:</strong> {{ user.id }}</p>
            <p><strong>Name:</strong> {{ user.name }}</p>
            <p><strong>Completed tasks:</strong> {{ user.completedTasks }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'ProfileView',
        data() {
            return {
                user: {
                    id: '',
                    name: '',
                    completedTasks: 0
                }
            }
        },
        async mounted() {
            await this.fetchProfile()
        },
        methods: {
            async fetchProfile(){
                try {
                    const tg_user = window.Telegram.webapp.initDataUnsafe?.user
                    const response = await fetch(`https://solid-space-waddle-jrj697xgx47fgxv-8000.app.github.dev/api/main/${tg_user.id}`)
                    const data = await response.json()
                    this.id = tg_user.id
                    this.name =tg_user.name
                    this.completedTasks = data.completedTasks                    
                } catch (error){
                    console.log(`error - ${error}`)
                }
            }
        }
    }
</script>

<style scoped>
 .profile-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 16px;
 }

 .profile-info {
    background-color: #ffffffcc;
    backdrop-filter: blur(8px);
    padding: 16px;
    border-radius: 8px;
    text-align: left;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-top: 16px;
    width: 100%;
    max-width: 320px;
 }
</style>