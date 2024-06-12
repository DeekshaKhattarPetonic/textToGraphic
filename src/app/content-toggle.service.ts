import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
  })
  export class ContentToggleService {
    showPromptTextArea: boolean = false;
  
    toggle() {
      this.showPromptTextArea = !this.showPromptTextArea;
    }
  }