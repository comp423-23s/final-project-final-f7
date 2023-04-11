import { Component, Inject } from '@angular/core';
import { Profile, ProfileService } from '../../profile/profile.service';
import { Workshop, WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { WorkshopDialogData } from '../workshop.component';

@Component({
  selector: 'app-workshop-dialog',
  templateUrl: './workshop-dialog.component.html',
  styleUrls: ['./workshop-dialog.component.css']
})
export class WorkshopDialogComponent {

  public profile: Profile | undefined

  constructor(
    protected profileService: ProfileService, 
    protected workshopService: WorkshopService,
    public dialogRef: MatDialogRef<WorkshopDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData
  ) {
    profileService.profile$.subscribe({
      next: (profile) => this.profile = profile,
    });
  }

  onSubmit(): void {
    let attendee = this.workshopService.registerUser(this.profile!, this.workshopDialogData.workshop);
    if (attendee !== null) {
      this.dialogRef.close();
    }
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
}
