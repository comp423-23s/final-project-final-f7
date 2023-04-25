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
  public isUserRegistered: boolean
  public allUsers: Profile[]

  constructor(
    protected profileService: ProfileService, 
    protected workshopService: WorkshopService,
    public dialogRef: MatDialogRef<WorkshopRegisterComponent>,
    protected snackBar: MatSnackBar,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData
  ) {
    this.allUsers = []
    profileService.profile$.subscribe({
      next: (profile) => this.profile = profile,
    });
    this.workshopService.checkRegister(this.workshopDialogData.workshop).subscribe( {
      next: (profileList) => {
        this.allUsers = profileList;
        this.isUserRegistered = profileList.filter(profile => profile.id === this.profile!.id).length >= 1 
      }
    });
    this.isUserRegistered = this.allUsers.includes(this.profile!)
  }

  onSubmit(): void {
    this.workshopService.registerUser(this.profile!, this.workshopDialogData.workshop).subscribe({
      next: () => this.onSuccess(),
      error: (err) => this.onError(err)
    });
    this.dialogRef.close();
  }
  
  onNoClick(): void {
    this.dialogRef.close();
  }

  private onSuccess() {
    this.snackBar.open(`You have been registered to ${this.workshopDialogData.workshop.title}!`, "", {duration: 2000});
  }

  private onError(err: any) {
    this.snackBar.open(`You are already registered to ${this.workshopDialogData.workshop.title}!`, "", {duration: 2000});
  }

}
