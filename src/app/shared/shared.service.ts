// shared.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private variable = new BehaviorSubject<boolean>(true); // Initial value is true
  currentVariable = this.variable.asObservable();

  constructor() { }

  setVariable(value: boolean) {
    this.variable.next(value);
  }
}
