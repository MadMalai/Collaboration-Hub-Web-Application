<template>
    <div>
        <h4>All Public Campaigns</h4>
    <br>
     
    <div class="searchtable">
    <input type="text" v-model="search">

    <table class="table" style="width: 75%;">
        <thead>
            <tr>
            <th scope="col">Campaign Details</th>
            <th scope="col">Action </th> 
            </tr>
        </thead>
        <tbody>
                <tr v-for="(cam, index) in filtereditems" :key="index">
                    <td><b>{{ cam['cam_name'] }} </b> - {{ cam['cam_desc'] }} - <b>Goals:</b> {{ cam['goals'] }}</td>
                    <td>
                        <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">View</router-link> 
                    </td>
                </tr>

        </tbody>
    </table>
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
      search:''
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
  computed:{
    filtereditems(){
      return this.campaigns.filter(cam => {
        return cam.cam_desc.indexOf(this.search) > -1
    })
  },
  },

  created() {
    this.roles = localStorage.getItem('roles');

    this.token = localStorage.getItem('authToken');
    if (!this.token) {
        this.$router.push('/')
    }

    this.getCampaigns() ;
  },
}



</script>
<style lang="">
    
</style>