import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.scss'
})
export class SidebarComponent {
  constructor(private contentToggleService: ContentToggleService) {}

  toggle() {
    this.contentToggleService.toggle();
  }
}
