import { Component, Inject } from '@angular/core';
import { Profile, ProfileService } from '../../profile/profile.service';
import { FormBuilder, Validators } from '@angular/forms';
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

  public registrationForm = this.formBuilder.group({
    first_name: "",
    last_name: "",
    email: "",
    pronouns: ""
  })

  constructor(
    protected profileService: ProfileService, 
    protected formBuilder: FormBuilder, 
    protected workshopService: WorkshopService,
    public dialogRef: MatDialogRef<WorkshopDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData) {

    profileService.profile$.subscribe({
      next: (profile) => this.profile = profile,
    });

    this.registrationForm.get('first_name')?.addValidators(Validators.required);
    this.registrationForm.get('last_name')?.addValidators(Validators.required);
    this.registrationForm.get('email')?.addValidators([Validators.required, Validators.email, Validators.pattern(/unc\.edu$/)]);
    this.registrationForm.get('pronouns')?.addValidators(Validators.required);
  }

  ngOnInit(): void {
    if (this.profile !== undefined) {
      this.registrationForm.setValue({
        first_name: this.profile.first_name,
        last_name: this.profile.last_name,
        email: this.profile.email,
        pronouns: this.profile.pronouns
      })
    }
  }

  onSubmit(): void {
    if (this.registrationForm.valid) {
      let attendee = this.workshopService.registerUser(
        this.registrationForm.value.first_name!,
        this.registrationForm.value.last_name!,
        this.registrationForm.value.email!,
        this.registrationForm.value.pronouns!,
        this.workshopDialogData.workshop
      );
      if (attendee) {
        this.dialogRef.close();
      }
    }
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
}
