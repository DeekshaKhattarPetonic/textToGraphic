import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { GenerateComponent } from './generate/generate.component';
import { PricingComponent } from './pricing/pricing.component';

const routes: Routes = [
  //{ path: '**', redirectTo: '' },
  { path: '', component: LandingPageComponent },
  { path: 'login', component: LoginComponent },
  { path:'signup', component: SignupComponent },
  { path: 'generate', component: GenerateComponent },
  {path: 'pricing', component: PricingComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
