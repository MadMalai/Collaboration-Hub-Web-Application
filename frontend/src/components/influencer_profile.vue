<template>
    <div>
        <div class="container mt-5">
            <div class="card">
                <div class="card-header">
                    <h2>Influencer Profile Details</h2>
                </div>
                <div class="card-body d-flex justify-content-between align-items-center">
                    <div class="card-body">
                        <p class="card-text"><b>Name:</b> {{ this.i_name}}</p>
                        <p class="card-text"><b>Platform Presence:</b> {{ this.i_presence }}</p>
                        <p class="card-text"><b>No. of Followers/Subscribers:</b> {{ this.i_follow_no  }}</p>
                        <p class="card-text"><b>Social Media Profile Link:</b> {{ this.i_link }}</p>
                        <p class="card-text"><b>Experience as Influencer(in years):</b> {{ this.i_exp  }}</p>
                        <p class="card-text"><b>Niche:</b> {{ this.i_niche  }}</p>
                        <p class="card-text"><b>Previous Brand Collabration:</b> {{ this.prev_brand_collab }}</p>
                        <p class="card-text"><b>Location:</b> {{ this.i_location  }}</p>
                        <p class="card-text"><b>Languages Spoken:</b> {{ this.i_language  }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios';

export default {

    name: 'influencer_profile',
  data() {
    return {
        i_name : '',
        i_presence:'',
        i_follow_no:null,
        i_link:'',
        i_exp:null,
        i_niche: '',
        prev_brand_collab:'',
        i_location:'',
        i_language:'',
        token: null,
        roles:[],
        userid:null
        }
  },

  methods: {
    viewInfluencerProfile() {
        axios
        .get(`http://127.0.0.1:5000/api/InfluencerSpecific/${this.userid}`,
        {headers: {Authorization: `${this.token}`}}
        )
        .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.var12 = response.data;
            this.i_name = response.data.data[0].i_name;
            this.i_presence = response.data.data[0].i_presence;
            this.i_follow_no = response.data.data[0].i_follow_no;
            this.i_link = response.data.data[0].i_link;
            this.i_exp = response.data.data[0].i_exp;
            this.i_niche = response.data.data[0].i_niche;
            this.prev_brand_collab = response.data.data[0].prev_brand_collab;
            this.i_location = response.data.data[0].i_location;
            this.i_language = response.data.data[0].i_language;
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
            if (this.roles=='influencer'){
                this.userid = localStorage.getItem('user_id');
            }
            else {
                this.userid = this.$route.params.id;
            }

            this.viewInfluencerProfile() ;
        },
}
</script>
<style lang="">
    
</style>