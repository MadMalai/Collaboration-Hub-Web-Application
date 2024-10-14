<template>
    <div class="mt-4"></div> 
    <h3> Welcome Admin! </h3>
    <div style="padding: 100px;">
    <h5>Active Campaigns</h5>
    <div class="mt-4"></div>    
    <div>
    <table class="table" id="camp_list">
      <thead>
        <tr>
        <th scope="col">Campaign ID</th>
        <th scope="col">Campaign Name</th>
        <th scope="col">Campaign Description</th>
        <th scope="col">Sponsor Name</th>
        <th scope="col">Progress</th>
        <th scope="col"></th> 
        </tr>
      </thead>
      <tbody>
            <tr v-for="(campaign, index) in cam_list" :key="index">
                <td>{{ campaign.cam_id }}</td>
                <td>{{ campaign.cam_name }}</td>
                <td>{{ campaign.cam_desc }}</td>
                <td>{{ campaign.org_name}}</td>
                <td>{{ campaign.progress }}</td>
                <td>
                <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: campaign['cam_id']}}">View</router-link>         
                </td>
                <td>
                    <button class="btn btn-danger" @click="flagCampaign(campaign.cam_id)" >Flag</button>
                </td>
              </tr>
      </tbody>
    </table>
    </div>
    <h5>List of Sponsors</h5>
    <div>
    <table class="table" id="camp_list">
      <thead>
        <tr>
        <th scope="col">Sponsor ID</th>
        <th scope="col">Sponsor Name</th>
        <th scope="col">Sponsor Industry</th>
        <th scope="col">Sponsor Organisation</th>
        <th scope="col"></th> 
        </tr>
      </thead>
      <tbody>
            <tr v-for="(sponsor, index) in spon_list" :key="index">
            <td>{{ sponsor.s_id }}</td>
            <td>{{ sponsor.s_name }}</td>
            <td>{{ sponsor.s_industry }}</td>
            <td>{{ sponsor.org_name }}</td>
            <!-- <td> -->
                <!-- <router-link class="btn btn-primary" :to="{ name: 'adminViewProfileDetails', params: { usertype, userid, s_id: sponsor.s_id, viewType: 2 } }">View</router-link>
            </td>
            <td>
                <router-link  class="btn btn-danger" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">Flag</router-link>
            </td> -->
            <td>
                <button class="btn btn-danger" @click="flagSponsor(sponsor.s_id)" >Flag</button>
            </td>
            </tr>
      </tbody>
    </table>
    </div>
    <h5>List of Influencers</h5>
    <div>
    <table class="table" id="camp_list">
      <thead>
        <tr>
        <th scope="col">Influencer ID</th>
        <th scope="col">Influencer Name</th>
        <th scope="col">Influencer Link</th>
        <th scope="col">Influencer Niche</th>
        <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(inf, index) in inf_list" :key="index">
            <td>{{ inf.i_id }}</td>
            <td>{{ inf.i_name }}</td>
            <td>{{ inf.i_link }}</td>
            <td>{{ inf.i_niche }}</td>
            <td>
                <button class="btn btn-danger" @click="flagInfluencer(inf.i_id)" >Flag</button>
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
    name: 'admin_find',
  data() {
    return {
      cam_list: [],
      spon_list: [],
      inf_list: [],
      token: null,
      roles:[]      
        }
  },
  methods: {

  getAdminFind() {
      const path = 'http://127.0.0.1:5000/api/AdminFind';
      axios
      .get(path,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.cam_list = response.data.cam_list;
            this.spon_list = response.data.spon_list;
            this.inf_list = response.data.inf_list;
        }         
        })
        .catch((error) => {
          console.error(error);
        });
    }, 
    flagCampaign(id){
        const path = 'http://127.0.0.1:5000/api/AdminFlagUser';
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
    flagSponsor(id){
        const path = 'http://127.0.0.1:5000/api/AdminFlagUser';
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
    flagInfluencer(id){
        const path = 'http://127.0.0.1:5000/api/AdminFlagUser';
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

    this.getAdminFind() ;
  },



}
</script>
<style lang="">
    
</style>




