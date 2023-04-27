/* Component that handles functionality of the delete dialog box. */

import { Component, Inject } from '@angular/core';
import { WorkshopDialogData } from '../workshop.component';
import { WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-workshop-delete',
  templateUrl: './workshop-delete.component.html',
  styleUrls: ['./workshop-delete.component.css']
})
export class WorkshopDeleteComponent {
  constructor(
  protected workshopService: WorkshopService,
    public dialogRef: MatDialogRef<WorkshopDeleteComponent>,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData,
    protected snackBar: MatSnackBar
  ){

  }

  onClick(): void {
    this.workshopService.deleteWorkshop(this.workshopDialogData.workshop).subscribe({
      next: () => this.onSuccess(),
    });
    this.dialogRef.close()
  }

  onNoClick(): void {
    this.dialogRef.close()
  }

  private onSuccess() {
    this.snackBar.open(`${this.workshopDialogData.workshop.title} Deleted!`, "", {duration: 2000})
  }  
}
