import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';

@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html',
  styleUrl: './generate.component.scss'
})
export class GenerateComponent {
  constructor(public contentToggleService: ContentToggleService) {}


  showPromptTextArea: boolean = false;

  toggle() {
    this.showPromptTextArea = !this.showPromptTextArea;
  }
  
}
