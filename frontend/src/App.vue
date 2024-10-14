<template>
  <div v-if="this.roles == null">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><b>Collaboration Hub</b></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link active" aria-current="page"  to="/">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/login_view">Login</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/signup_view">Signup</router-link>
              </li>
            </ul>
          </div>
        </div>
        <div class="tagline">Influencer Engagement & Sponsorship Co-ordination Platform</div>
    </nav>
  </div>
  <div v-else-if="this.roles=='sponsor'">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><b>Collaboration Hub</b></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link active" aria-current="page"  to="/sponsor_home">Sponsor Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/sponsor_profile">Profile</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/campaign_home">Campaign</router-link>

              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/sponsor_find">Find</router-link>

              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="#">Stats</router-link>

              </li>
              <li class="nav-item">
                <a href class="nav-link" @click="logoutfn">Logout</a>

                
              </li>
            </ul>
          </div>
        </div>
        <div class="tagline">Influencer Engagement & Sponsorship Co-ordination Platform</div>
    </nav>

  </div>
  <div v-else-if="this.roles=='influencer'">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><b>Collaboration Hub</b></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link active" aria-current="page"  to="/influencer_home">Influencer Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/influencer_profile">Profile</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/influencer_find">Find</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="#">Stats</router-link>
              </li>
              <li class="nav-item">
                <a href class="nav-link" @click="logoutfn">Logout</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="tagline">Influencer Engagement & Sponsorship Co-ordination Platform</div>
    </nav>

  </div>

  <div v-else-if="this.roles=='admin'">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><b>Collaboration Hub</b></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link class="nav-link active" aria-current="page"  to="/admin_home">Admin Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/admin_find">Find</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/admin_stat">Stats</router-link>
              </li>
              <li class="nav-item">
                <a href class="nav-link" @click="logoutfn">Logout</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="tagline">Influencer Engagement & Sponsorship Co-ordination Platform</div>
    </nav>

  </div>
  <router-view/>
</template>


<script>
export default{
  data() {
    return {
      roles:'',
    }
  },
  methods:{

      logoutfn(){
        localStorage.clear()
        this.$router.push('/')
      }
    },
  created() {
  this.roles = localStorage.getItem('roles');
},

};
//import { RouterView } from 'vue-router'
</script>