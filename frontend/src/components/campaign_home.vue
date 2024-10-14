<template>
    <div>
        <div class="container mt-5">
        <h2>Campaign Details</h2>
        <p><router-link  class="btn btn-primary" :to="{name: 'create_campaign'}">Create New Campaign</router-link> </p>
      </div>

      <div class="container mt-5 mb-5">
          <div class="row row-cols-4 row-cols-md-8 g-4 mb-4">
            <div v-for="(cam, index) in campaigns" :key="index">
                <div class="row justify-content-center mt-4 mb-4"> 
                  <div class="card"  style="width: 18rem;" >
                    <h3 class="card-header">{{cam.cam_name }}</h3>
                        <div class="card-body">
                          <p class="card-text">This campaign is to {{ cam.cam_desc }}.</p>
                          <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">View</router-link> 
                        </div>  
                  </div>
            </div>
          </div>
      </div>
    </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'sponsor_home',
  data() {
    return {
      campaigns: [],
      token: null,
      roles:[],
        }
  },
  methods: {

  getCampaigns() {
      const path = 'http://127.0.0.1:5000/api/CampaignResource';
      axios
      .get(path,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.campaigns = response.data.data;
        }
          
        })
        .catch((error) => {
          console.error(error);
        });
    },
    logoutfn(){
        localStorage.clear()
        this.$router.push('/')
      },
  },

  created() {
    this.token = localStorage.getItem('authToken');
    if (!this.token) {
        this.$router.push('/')
    }
    this.roles = localStorage.getItem('roles');

    this.getCampaigns() ;
  },

}
</script>
<style lang="">
    
</style>