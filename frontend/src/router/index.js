import { createRouter, createWebHistory } from 'vue-router'
import sponsor_home from '@/components/sponsor_home.vue'
import welcomePage from '@/components/welcomePage.vue'

import login_view from '@/components/login_view.vue'
import signup_view from '@/components/signup_view.vue'

import create_sponsor_details from '@/components/create_sponsor_details.vue'
import sponsor_profile from '@/components/sponsor_profile.vue'
import campaign_home from '@/components/campaign_home.vue'
import create_campaign from '@/components/create_campaign.vue'
import sponsor_find from '@/components/sponsor_find.vue'


import viewCampaignDetail from '@/components/viewCampaignDetail.vue'
import edit_campaign from '@/components/edit_campaign.vue'

import create_ad from '@/components/create_ad.vue'
import edit_ad from '@/components/edit_ad.vue'

import create_influencer_details from '@/components/create_influencer_details.vue'
import influencer_profile from '@/components/influencer_profile.vue'
import influencer_home from '@/components/influencer_home.vue'
import influencer_stats from '@/components/influencer_stats.vue'
import influencer_find from '@/components/influencer_find.vue'
import admin_home from '@/components/admin_home.vue'
import admin_find from '@/components/admin_find.vue'
import admin_stat from '@/components/admin_stat.vue'





const routes = [
  {
    path: '/',
    name: 'welcomePage',
    component: welcomePage
  },
  {
    path: '/login_view',
    name: 'login_view',
    component: login_view
  },
  {
    path: '/signup_view',
    name: 'signup_view',
    component: signup_view
  },
  {
    path: '/create_sponsor_details/:s_id',
    name: 'create_sponsor_details',
    component: create_sponsor_details
  },
  {
    path: '/create_influencer_details/:i_id',
    name: 'create_influencer_details',
    component: create_influencer_details
  },
  {
    path: '/admin_home',
    name: 'admin_home',
    component: admin_home
  },
  {
    path: '/sponsor_home',
    name: 'sponsor_home',
    component: sponsor_home
  },
  {
    path: '/sponsor_profile',
    name: 'sponsor_profile',
    component: sponsor_profile
  },
  {
    path: '/sponsor_profile/:id',
    name: 'sponsor_profile_with_id',
    component: sponsor_profile
  },
  {
    path: '/sponsor_find',
    name: 'sponsor_find',
    component: sponsor_find
  },
  {
    path: '/campaign_home',
    name: 'campaign_home',
    component: campaign_home
  },
  {
    path: '/create_campaign',
    name: 'create_campaign',
    component: create_campaign
  },
  {
    path: '/viewCampaignDetail/:cam_id',
    name: 'viewCampaignDetail',
    component: viewCampaignDetail
  },
  {
    path: '/edit_campaign/:cam_id',
    name: 'edit_campaign',
    component: edit_campaign
  },
  {
    path: '/create_ad/:cam_id',
    name: 'create_ad',
    component: create_ad
  },
  {
    path: '/edit_ad/:ad_id',
    name: 'edit_ad',
    component: edit_ad
  },
  {
    path: '/influencer_profile',
    name: 'influencer_profile',
    component: influencer_profile
  },
  {
    path: '/influencer_profile/:id',
    name: 'influencer_profile_with_id',
    component: influencer_profile
  },
  {
    path: '/influencer_home',
    name: 'influencer_home',
    component: influencer_home
  },
  {
    path: '/influencer_stats',
    name: 'influencer_stats',
    component: influencer_stats
  },
  {
    path: '/influencer_find',
    name: 'influencer_find',
    component: influencer_find
  },
  {
    path: '/influencer_profile',
    name: 'influencer_profile',
    component: influencer_profile
  },
  {
    path: '/admin_home',
    name: 'admin_home',
    component: admin_home
  },
  {
    path: '/admin_find',
    name: 'admin_find',
    component: admin_find
  },
  {
    path: '/admin_stat',
    name: 'admin_stat',
    component: admin_stat
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
