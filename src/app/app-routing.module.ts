import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { GenerateComponent } from './generate/generate.component';
import { PricingComponent } from './pricing/pricing.component';
import { LandingPageComponent2 } from './landing-page2/landing-page2.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './profile/profile.component';
const routes: Routes = [
  //{ path: '**', redirectTo: '' },
  { path: 'home', component: LandingPageComponent },
  // { path: 'home', component: LandingPageComponent },
  { path: 'login', component: LoginComponent },
  { path:'signup', component: SignupComponent },
  { path: 'generate', component: GenerateComponent },
  // { path: 'generate-light', component: LandingPageComponent2 },
  {path: 'pricing', component: PricingComponent},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'profile', component: ProfileComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
