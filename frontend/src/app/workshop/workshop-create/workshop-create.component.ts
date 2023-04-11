import { Component, Inject } from '@angular/core';
import { Workshop, WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { WorkshopDialogData } from '../workshop.component';

@Component({
  selector: 'app-workshop-create',
  templateUrl: './workshop-create.component.html',
  styleUrls: ['./workshop-create.component.css']
})
export class WorkshopCreateComponent {

  public workshop: Workshop | undefined

  constructor(
    protected workshopService: WorkshopService
  ){
    workshopService.workshop$.subscribe({
      // TODO
    });
  }

  onSubmit(): void {
    let workshop_new = this.workshopService.createWorkshop()
  }

}
