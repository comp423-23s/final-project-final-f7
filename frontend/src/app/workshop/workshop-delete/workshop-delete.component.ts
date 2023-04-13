import { Component, Inject } from '@angular/core';
import { WorkshopDialogData } from '../workshop.component';
import { Workshop, WorkshopService } from '../workshop.service';
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
    this.workshopService.delete_workshop(this.workshopDialogData.workshop).subscribe({
      next: () => this.onSuccess(),
      error: (err) => this.onError(err)
    });
    this.dialogRef.close()
  }

  onNoClick(): void {
    this.dialogRef.close()
  }

  private onSuccess(){
    this.snackBar.open(`${this.workshopDialogData.workshop.title} Deleted!`, "", {duration: 2000})
  }

  private onError(err: any){
  }
  
}

