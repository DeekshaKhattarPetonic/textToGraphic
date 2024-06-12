import { Component } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'text-to-graphic';
  isLoginPage: boolean = true;
  isSignUpPage: boolean = true;
  isLandingPage: boolean = false;
  constructor(private router: Router,) { }


  ngOnInit() {
    this.router.events
      .pipe(filter((event: any) => event instanceof NavigationEnd))
      .subscribe((event: NavigationEnd) => {
       
        this.isLoginPage = event.url === '/login';
        this.isSignUpPage = event.url === '/signup';
        this.isLandingPage = event.url === '/';
       // this.isMindMapPage = event.url === '/mindmap' || event.url === '/mind-map-new-tab';
        //this.isflowchartPage = event.url === '/flowchart';
      });
  
  
  }

}


