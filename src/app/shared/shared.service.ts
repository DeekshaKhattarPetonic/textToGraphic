// shared.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private variable = new BehaviorSubject<boolean>(true); // Initial value is true
  currentVariable = this.variable.asObservable();

  private mode = new BehaviorSubject<any>('textToImage'); // Initial value is true
  currentMode = this.mode.asObservable();

  private imgUrl = new BehaviorSubject<any>(''); // Initial value is true
  currentImgUrl = this.imgUrl.asObservable();

  constructor() { }

  setVariable(value: boolean) {
    this.variable.next(value);
  }

   setMode(value: any) {
    this.mode.next(value);
  }

   setUploadedImageUrl(value: any) {
    this.imgUrl.next(value);
  }


}
