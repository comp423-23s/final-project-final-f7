/* Component that handles functionality of the registration dialog box that appears when clicking the register button. */

import { Component, Inject } from '@angular/core';
import { Profile, ProfileService } from '../../profile/profile.service';
import { WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { WorkshopDialogData } from '../workshop.component';

@Component({
  selector: 'app-workshop-register',
  templateUrl: './workshop-register.component.html',
  styleUrls: ['./workshop-register.component.css']
})
export class WorkshopRegisterComponent {

  public profile: Profile | undefined  // Holds the profile currently logged in.

  constructor(
    protected profileService: ProfileService, 
    protected workshopService: WorkshopService,
    public dialogRef: MatDialogRef<WorkshopRegisterComponent>,
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
