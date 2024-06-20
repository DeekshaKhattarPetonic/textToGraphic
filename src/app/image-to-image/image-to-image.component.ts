import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-image-to-image',
  templateUrl: './image-to-image.component.html',
  styleUrl: './image-to-image.component.scss'
})

export class ImageToImageComponent {
  imageUrlToDownload: any = '';
  uploadedImageUrl: any = '';
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
    { image: "../../assets/img/img-3.jpg" },
    { image: "../../assets/img/img-4.jpg" },
    { image: "../../assets/img/img-6.jpg" },
    { image: "../../assets/img/img-7.jpg" },
    // {image: "../../assets/img/img-5.jpg"},
    // {image: "../../assets/img/img-3.jpg"},
    // {image: "../../assets/img/img-3.jpg"},
  ]

  constructor(private sharedService: SharedService, public contentToggleService: ContentToggleService) { }

  ngOnInit() {
    this.sharedService.currentVariable.subscribe(value => {
      this.defaultView = value;
    });

    this.sharedService.currentImgUrl.subscribe(value => {
      this.uploadedImageUrl = value;
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


  confirm() {
    // this.showVersion = true
    this.showConfirmationModal = false
    this.showVersion = true
  }

  showImageVersions() {
    this.modalText = 'Do you want to proceed?';
    this.showConfirmationModal = true
    // this.showVersion = true
    // this.defaultView = true
  }

  onVersionChange() {
    console.log('Selected version:', this.selectedVersion);
  }

  onCancel() {
    this.defaultView = true
    this.showVersion = false
  }

  goBack() {
    this.defaultView = false;
    this.showVersion = false;
  }

  onImageSelectionChange(event: any) {
    const inputElement = event.target as HTMLInputElement;
    this.imageUrlToDownload = inputElement.value;

    const selectedImage = event.target.value;
    if (selectedImage === 'image1') {
      this.selectedImageSrc = '../../assets/img/img-4.jpg';
    }
    // Add additional conditions for other images
  }


  downloadImage() {
    let imageUrl: string;
    switch (this.imageUrlToDownload) {
      case 'image1':
        imageUrl = this.uploadedImageUrl; // URL for Image 1
        break;
      case 'image2':
        imageUrl = this.uploadedImageUrl; // URL for Image 2
        break;
      case 'image3':
        imageUrl = this.uploadedImageUrl; // URL for Image 3
        break;
      case 'image4':
        imageUrl = this.uploadedImageUrl; // URL for Image 4
        break;
      default:
        imageUrl = this.uploadedImageUrl;
    }
    this.triggerDownload(imageUrl);
  }

  triggerDownload(url: string) {
    const link = document.createElement('a');
    link.href = url;
    link.download = 'downloadedImage.jpg';
    link.click();
  }
}
