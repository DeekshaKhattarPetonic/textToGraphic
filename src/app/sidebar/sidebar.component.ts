import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.scss'
})
export class SidebarComponent {
  constructor(private sharedService: SharedService, private contentToggleService: ContentToggleService) {}

  toggle() {
    this.contentToggleService.toggle();
  }

  onButtonClick() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    this.sharedService.setVariable(false);
  }
}
