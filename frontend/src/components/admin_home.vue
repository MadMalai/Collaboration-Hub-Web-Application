<template>
  <div>
      <div class="mt-4"></div>
      <h3> Welcome Admin! </h3>
      <div class="mb-4"></div>

      <h5><b>Activate Users</b></h5>

      <div v-for="(usr, index) in deactivated_users" :key="index">

      <div class="row">
          <div class="col-md-*">
              <div class="card">
                  <div class="card-body d-flex justify-content-between align-items-center">
                      <div class="card-title"><b>User Details {{ usr['id'] }} </b> | {{ usr.email }}</div>
                      <button class="btn btn-danger" @click="activate( usr['id'])">Activate</button> 
                  </div>
              </div>
            </div>
          </div>
        </div>
        <br>
        <br>


      <h5>Active Campaigns</h5> 
      <div class="mb-4"></div>
      <div class="container mt-4">
          <div class="row">
          <div 
              v-for="(campaign, index) in cam_list" 
              :key="index" 
              class="col-md-*">
              <!-- Card -->
              <div class="card">
              <div class="card-body d-flex justify-content-between align-items-center">
                  <h5 class="card-title">
                  Campaign {{ campaign.cam_id }} | {{ campaign.cam_name }} | Progress {{ campaign.progress }} %
                  </h5>
                  <router-link 
                  class="btn btn-primary" 
                  :to="{name: 'viewCampaignDetail', params: {cam_id: campaign['cam_id']}}">
                  View
                  </router-link>
              </div>
              </div>
          </div>
          </div>
      </div>
  </div>

    <h5><b>List of Flagged Users / Campaigns</b></h5>

    <div class="container mt-4">
      <!-- Influencers -->
      <div class="row">
        <div v-for="(inf, index) in flagged_inf" :key="index" class="col-md-*">
          <div class="card">
            <div class="card-body d-flex justify-content-between align-items-center">
              <h5 class="card-title">Influencer Name: {{ inf.i_name }} | {{ inf.i_link }}</h5>
              <div>
               <router-link  class="btn btn-primary" :to="{name: 'influencer_profile_with_id', params: {id: inf.i_id}}">View</router-link> 

                <td>
                <button class="btn btn-danger" @click="unFlagInfluencer(inf.i_id)" >Unflag</button>
                </td>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sponsors -->
      <div class="row">
        <div v-for="(spon, index) in flagged_spon" :key="index" class="col-md-*">
          <div class="card">
            <div class="card-body d-flex justify-content-between align-items-center">
              <h5 class="card-title">Sponsor Name: {{ spon.s_name }} | {{ spon.org_name }}</h5>
              <div>
                <router-link  class="btn btn-primary" :to="{name: 'sponsor_profile_with_id', params: {id: spon.s_id}}">View</router-link> 

                <!-- <router-link 
                  class="btn btn-primary" 
                  :to="{name: 'adminViewProfileDetails', params: { usertype, userid, id: spon.s_id, type: 2 }}">
                  View
                </router-link> -->
                <td>
                <button class="btn btn-danger" @click="unFlagSponsor(spon.s_id)" >Unflag</button>
                </td
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Campaigns -->
      <div class="row">
        <div v-for="(cam, index) in flagged_cam" :key="index" class="col-md-*">
          <div class="card">
            <div class="card-body d-flex justify-content-between align-items-center">
              <h5 class="card-title">Campaign Name: {{ cam.cam_name }} | {{ cam.cam_category }}</h5>
              <div>
                <router-link 
                  class="btn btn-primary" 
                  :to="{name: 'viewCampaignDetail', params: {cam_id: cam.cam_id }}">
                  View
                </router-link>
                <td>
                <button class="btn btn-danger" @click="unFlagCampaign(cam.cam_id)" >Unflag</button>
                </td
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
  name: 'admin_find',
data() {
  return {
    cam_list: [],
    flagged_inf: [],
    flagged_spon: [],
    flagged_cam: [],
    token: null,
    roles:[] ,
    deactivated_users:[],    
      }
},
methods: {
  getUsers() {
      const path = 'http://127.0.0.1:5000/api/activateManager';
      axios.get(path,{headers: {Authorization: `${this.token}`}})
        .then((res) => {
          this.deactivated_users = res.data.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    activate(id) {
      const path = 'http://127.0.0.1:5000/api/activateManager';
      axios.post(path,{"id":id},{headers: {Authorization: `${this.token}`}})
        .then((res) => {
          this.campaigns = res.data.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },

getAdminHomeDetails() {
    const path = 'http://127.0.0.1:5000/api/AdminHomeDetails';
    axios
    .get(path,
          {headers: {Authorization: `${this.token}`}})
    .then((response) => {
      console.log("response block", response)
      if (response.status == 200) {
          this.cam_list = response.data.cam_list;
          this.flagged_inf = response.data.flagged_inf;
          this.flagged_spon = response.data.flagged_spon;
          this.flagged_cam = response.data.flagged_cam;
      }         
      })
      .catch((error) => {
        console.error(error);
      });
  }, 
  unFlagCampaign(id){
      const path = 'http://127.0.0.1:5000/api/AdminUnFlagUser';
    axios
    .put(path,{"objecttype":"1" ,"objectid":id },
          {headers: {Authorization: `${this.token}`}})
    .then((response) => {
      console.log("response block", response)
      if (response.status == 200) {

      }         
      })
      .catch((error) => {
        console.error(error);
      });        
  },
  unFlagSponsor(id){
      const path = 'http://127.0.0.1:5000/api/AdminUnFlagUser';
    axios
    .put(path,{"objecttype":"2" ,"objectid":id },
          {headers: {Authorization: `${this.token}`}})
    .then((response) => {
      console.log("response block", response)
      if (response.status == 200) {
      }         
      })
      .catch((error) => {
        console.error(error);
      });        
  },
  unFlagInfluencer(id){
      const path = 'http://127.0.0.1:5000/api/AdminUnFlagUser';
    axios
    .put(path,{"objecttype":"3" ,"objectid":id },
          {headers: {Authorization: `${this.token}`}})
    .then((response) => {
      console.log("response block", response)
      if (response.status == 200) {

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

  this.getAdminHomeDetails() ;
  this.getUsers();

},



}
</script>
<style lang="">
  
</style>




