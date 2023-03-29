import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkshopListsComponent } from './workshop-lists.component';

describe('WorkshopListsComponent', () => {
  let component: WorkshopListsComponent;
  let fixture: ComponentFixture<WorkshopListsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WorkshopListsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WorkshopListsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
