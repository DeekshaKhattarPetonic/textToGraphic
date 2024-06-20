import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.scss'
})
export class LandingPageComponent implements OnInit{
  images: any;
  industries: any = [];
  responsiveOptions: any[] | undefined;
  products: any;
  selectedIndustry: any = 'Interior Design';
  industry: any = '';

  constructor(){
    this.images = [
      {image:   '../../assets/img/interior/i1.jpg'},
      {image:   '../../assets/img/interior/i2.jpg'},
      {image:   '../../assets/img/interior/i3.avif'},

      {image:   '../../assets/img/interior/i4.webp'},
      {image:   '../../assets/img/interior/i5.jpg'},
      {image:   '../../assets/img/interior/i6.jpg'},

      {image:   '../../assets/img/interior/i7.jpg'},
      {image:   '../../assets/img/interior/i8.jpg'},
      {image:   '../../assets/img/interior/i9.jpg'},

     ]
     this.repeatImages(8)
  }

  ngOnInit(): void{
    // this.startAutoPlay();

this.industries = [
  'Interior Design',
  'Advertising',
  'Marketing',
  'Media & Publishing',
  'Fashion',
  'Entertainment', 'Web & App Development',
  'Corporate', 'Packaging',
  'Education', 'Healthcare',
  'Hospitality', 'Sports',
  'Retail', 'Technology',
  'Real Estate', 'Architecture',
  'Automotive', 'Non-Profit',
  'Food & Beverage', 'Textile and Garment Design',
  'Sports',
]
  }


changeIndustry(industry : any){
this.selectedIndustry = industry


console.log(this.selectedIndustry)
}

applyFilter(){
  if(this.selectedIndustry == 'Fashion'){
    this.images = [
      {image:   '../../assets/img/fashion/f-1.avif'},
      {image:   '../../assets/img/fashion/f2.webp'},
      {image:   '../../assets/img/fashion/f3.webp'},
      {image:   '../../assets/img/fashion/f4.jpg'},
      {image:   '../../assets/img/fashion/f5.jpg'},
      {image:   '../../assets/img/fashion/f6.jpg'},
      {image:   '../../assets/img/fashion/f7.jpg'},
      {image:   '../../assets/img/fashion/f8.webp'},
      ]
      this.repeatImages(8)
  }

  if(this.selectedIndustry == 'Textile and Garment Design'){
    this.images = [
      {image:   '../../assets/img/textile/t1.jpg'},
      {image:   '../../assets/img/textile/t2.jpg'},
      {image:   '../../assets/img/textile/t3.jpg'},
      {image:   '../../assets/img/textile/t4.jpg'},
      {image:   '../../assets/img/textile/t5.jpg'},
      {image:   '../../assets/img/textile/t6.jpg'},
      {image:   '../../assets/img/textile/t7.jpg'},
      {image:   '../../assets/img/textile/t8.jpg'},
      ]
      this.repeatImages(8)
  }

  if(this.selectedIndustry == 'Interior Design'){
    this.images = [
      {image:   '../../assets/img/interior/i1.jpg'},
      {image:   '../../assets/img/interior/i2.jpg'},
      {image:   '../../assets/img/interior/i3.avif'},

      {image:   '../../assets/img/interior/i4.webp'},
      {image:   '../../assets/img/interior/i5.jpg'},
      {image:   '../../assets/img/interior/i6.jpg'},

      {image:   '../../assets/img/interior/i7.jpg'},
      {image:   '../../assets/img/interior/i8.jpg'},
      {image:   '../../assets/img/interior/i9.jpg'},
      ]
      this.repeatImages(8)
  }
}

repeatImages(repeatCount: number) {
  const originalLength = this.images.length;
  const repeatedImages = [];

  for (let i = 0; i < repeatCount; i++) {
    for (let j = 0; j < originalLength; j++) {
      repeatedImages.push(this.images[j]);
    }
  }

  this.images = repeatedImages;
}
}
