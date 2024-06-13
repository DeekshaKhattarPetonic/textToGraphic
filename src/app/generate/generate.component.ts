import { Component } from '@angular/core';
import { ContentToggleService } from '../content-toggle.service';
import { SharedService } from '../shared/shared.service';



@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html',
  styleUrl: './generate.component.scss'
})
export class GenerateComponent {
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

onImageSelectionChange(event: Event): void{
//  this.showConfirmationModal = true;
//  console.log('showConfirmationModal', this.showConfirmationModal)
}

confirm(){
  // this.showVersion = true
  this.showConfirmationModal = false
  this.showVersion = true
}

showImageVersions(){
this.showConfirmationModal = true
  // this.showVersion = true
  // this.defaultView = true
}
}
