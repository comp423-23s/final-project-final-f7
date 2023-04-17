/* Component that handles functionality of the registration dialog box that appears when clicking the register button. */

import { Component, Inject } from '@angular/core';
import { Profile, ProfileService } from '../../profile/profile.service';
import { WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { WorkshopDialogData } from '../workshop.component';
import { MatSnackBar } from '@angular/material/snack-bar';

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
    protected snackBar: MatSnackBar,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData
  ) {
    profileService.profile$.subscribe({
      next: (profile) => this.profile = profile,
    });
  }

  onSubmit(): void {
    this.workshopService.registerUser(this.profile!, this.workshopDialogData.workshop.id).subscribe({
      next: () => this.onSuccess(),
      error: (err) => this.onError(err)
    });
    this.dialogRef.close();
  }
  
  onNoClick(): void {
    this.dialogRef.close();
  }

  private onSuccess() {
    this.snackBar.open(`You have been registered to ${this.workshopDialogData.workshop.title}!`, "", {duration: 2000})
  }

  private onError(err: any) {
    // TODO: Handle this in some way.
  }

}
