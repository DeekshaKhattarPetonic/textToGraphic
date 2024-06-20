import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LandingPageComponent2 } from './landing-page2.component';

describe('LandingPageComponent', () => {
  let component: LandingPageComponent2;
  let fixture: ComponentFixture<LandingPageComponent2>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LandingPageComponent2]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LandingPageComponent2);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
