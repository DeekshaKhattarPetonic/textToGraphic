import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-text-to-image',
  templateUrl: './text-to-image.component.html',
  styleUrl: './text-to-image.component.scss'
})

export class TextToImageComponent {
  selectedImageSrc: any = '';
  selectedOption: any = 'Select Version';
  modalText: any = '';
  selectedVersion: any = 1;
  versions: string[] = ['1', '2'];
  showConfirmationModal: any = false;
  // variable: any;
  showVersion: any = false;
  responsiveOptions: any[] | undefined;
  defaultView: any = true;
  products: any = [
    {image: "../../assets/img/img-3.jpg"},
    {image: "../../assets/img/img-4.jpg"},
    {image: "../../assets/img/img-6.jpg"},
    {image: "../../assets/img/img-7.jpg"},
    // {image: "../../assets/img/img-5.jpg"},
    // {image: "../../assets/img/img-3.jpg"},
    // {image: "../../assets/img/img-3.jpg"},
  ]

  constructor(private sharedService: SharedService, public contentToggleService: ContentToggleService) {}

ngOnInit(){
  this.sharedService.currentVariable.subscribe(value => {
    this.defaultView = value;
  });

  this.responsiveOptions = [
    {
        breakpoint: '1199px',
        numVisible: 3,
        numScroll: 3
    },
    {
        breakpoint: '991px',
        numVisible: 3,
        numScroll: 3
    },
    {
        breakpoint: '767px',
        numVisible: 3,
        numScroll: 3
    }
];
}

  showPromptTextArea: boolean = false;

  toggle() {
    this.showPromptTextArea = !this.showPromptTextArea;
  }

  getSeverity(status: string): any {
    switch (status) {
        case 'INSTOCK':
            return 'success';
        case 'LOWSTOCK':
            return 'warning';
        case 'OUTOFSTOCK':
            return 'danger';
    }
}


confirm(){
  // this.showVersion = true
  this.showConfirmationModal = false
  this.showVersion = true
}

showImageVersions(){
  this.modalText = 'Do you want to proceed?';
this.showConfirmationModal = true
  // this.showVersion = true
  // this.defaultView = true
}

onVersionChange() {
  console.log('Selected version:', this.selectedVersion);
}

onCancel(){
  this.defaultView = true
  this.showVersion = false
}

goBack(){
  this.defaultView = false;
  this.showVersion = false;
}

onImageSelectionChange(event: any) {
  const selectedImage = event.target.value;
  // Update `selectedImageSrc` based on the selected image
  // This is a placeholder, replace with actual logic to set the selected image
  if (selectedImage === 'image1') {
    this.selectedImageSrc = '../../assets/img/img-4.jpg';
  }
  // Add additional conditions for other images
}

downloadImage() {
  const link = document.createElement('a');
  link.href = this.selectedImageSrc;
  link.download = this.selectedImageSrc.split('/').pop()!;
  link.click();
}
}
