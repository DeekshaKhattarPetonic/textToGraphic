import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.scss'
})

export class SidebarComponent {
  fileName: string = '';
  selectedVersion: any;
  imageSrc: any | ArrayBuffer | null = '';
  showCard: any = false;
  selectedIndustry: any = '';
  selectedCategory: any = '';
  selectedResolution: any = '';
  selectedColorDepth: any = '';
  selectedDpi: any = '';
  selectedRatio: any = '';
  customerSegment: any = '';
  purpose: any = '';
  imgRatio: any = '';
  imgColorDepth: any = '';
  showImageCard: any = false;
  imgResolution: any = '';
  imgDpi: any = '';
  area: any = '';

  constructor(private sharedService: SharedService, private contentToggleService: ContentToggleService) { }

  toggle() {
    this.contentToggleService.toggle();
  }

  onGenerateImage(type: any) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    this.sharedService.setVariable(false);


    if (type == 'image') {
      this.sharedService.setMode('imageToImage');
      this.showImageCard = true;
    }

    if (type == 'text') {
      this.sharedService.setMode('textToImage');
      this.showCard = true;
    }
  }

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];

    if (file) {
      this.fileName = file.name;

      const reader = new FileReader();
      reader.onload = (e) => {
        this.imageSrc = e.target?.result;
        this.sharedService.setUploadedImageUrl(this.imageSrc);
      };

      reader.readAsDataURL(file);
    }
  }
}
