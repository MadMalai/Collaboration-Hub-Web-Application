<template>

  <div class="container mt-2" style="padding: 100px">
    <form @submit.prevent="submitForm">
      <p>{{ this.resp_message}}</p>
      <div class="row mt-2">
        <h5> List of Influencers </h5>
        <div class="searchtable">
          <input type="text" v-model="search" >
          <table class="table" id="inf_list">
            <thead>
                <tr>
                <th scope="col">Name</th>
                <th scope="col">Link</th>
                <th scope="col">Niche</th>
                <th scope="col">Followers</th>
                <th scope="col"></th> 
                </tr>
            </thead>
            <tbody>
                    <tr v-for="(inf, index) in filtereditems" :key="index">
                        <td>{{ inf.i_name }}</td>
                        <td>{{ inf.i_link }}</td>
                        <td>{{ inf.i_niche }}</td>
                        <td>{{ inf.i_follow_no }}</td>
                        <td>
                        <router-link  class="btn btn-primary" :to="{name: 'influencer_profile_with_id', params: {id: inf.i_id}}">View</router-link> 
                        </td>
                        <td>
                          <input type="radio" :id="'radio' + index" :value="inf.i_id" v-model="this.i_id">
                        </td>
                      </tr>
            </tbody>
        </table>
        </div>

      </div>

      <div class="row mt-3 ">
      <h5> Select Campaign </h5>
      <div class="col-6 ">
        <select v-model="this.cam_id" @change="viewAds">
          <option v-for="(cam, index) in campaigns" :key="index" :value= "cam.cam_id" >{{ cam.cam_name }}</option>
        </select>
      </div>
 
      </div>
      
      <div class="row mt-3 ">
      <h5> Select Ad </h5>
      <div class="col-6 " style="width: 150%;">
        <select v-model="this.ad_id">
          <option v-for="(ad, index) in ad_list" :key="index" :value= "ad.ad_id" >{{ ad.ad_name }}</option>
        </select>
      </div>
 
      </div>


      <div class="row mt-4">
        <h5> Enter Message for Influencers </h5>
        <input type="text" class="form-control" v-model="this.req_msg" required>
      </div>

      <div class="row mt-5">
        <div class="col-6 col-md-4"><button class="btn btn-primary"  @click="requestInfluencer">Send Request</button> </div>
        
      </div>
    </form>
    </div>

</template>
<script>
import axios from 'axios';

export default {
    name: 'sponsor_find',
  data() {
    return {
      inf_list: [],
      token: null,
      roles:[],
      campaigns:[],
      ad_list:[],
      ad_id:null,
      i_id:null,
      cam_id:null,
      req_msg: '',
      resp_message:'',
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
    getInfluencers() {
      const path = 'http://127.0.0.1:5000/api/InfluencerResource';
      axios
      .get(path,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.inf_list = response.data.data;
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
    requestInfluencer(){

        const path = 'http://127.0.0.1:5000/api/Ad_request';
      axios
      .post(path,{
        cam_id:this.cam_id,
        i_id:this.i_id,
        ad_id:this.ad_id,
        req_msg:this.req_msg
      },
      {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status === 201) {
          this.resp_message="Request Sent"
          this.cam_id=null,
          this.i_id=null,
          this.ad_id=null,
          this.req_msg=''
          location.reload();

        }
        else if (response.status === 200) {
          this.resp_message="Already Request Sent in the past!"

        }
        else{
          this.resp_message="error"
        }
        })
        .catch((error) => {
          console.error(error);
        });

      },
    viewAds() {
      axios
      .get(`http://127.0.0.1:5000/api/AdResource/${this.cam_id}`,
      {headers: {Authorization: `${this.token}`}}
      )
      .then((response) => {
      console.log("response block", response)
      if (response.status == 200) {
          this.ad_list = response.data.data;
      }
          
      })
      .catch((error) => {
          console.error(error);
      });
  },    
  },
  computed:{
    filtereditems(){
      return this.inf_list.filter(inf => {
        return inf.i_niche.indexOf(this.search) > -1
    })
  },
  },

  created() {
    this.token = localStorage.getItem('authToken');
    if (!this.token) {
        this.$router.push('/')
    }
    this.roles = localStorage.getItem('roles');
    this.getCampaigns();
    this.getInfluencers() ;
  },
  
}
</script>
<style lang="css">
    .form-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 20px;
  border: 1px solid #ccc;
}

.table-container {
  height: 300px; /* Set the desired height for the table container */
  overflow-y: auto; /* Add vertical scroll if the table content exceeds the container height */
}
</style>