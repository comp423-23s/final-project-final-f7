/* Component handling functionality of the dialog box that is displayed upon clicking the create button. */

import { Component } from '@angular/core';
import { Workshop, WorkshopService } from '../workshop.service';
import { MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-workshop-create',
  templateUrl: './workshop-create.component.html',
  styleUrls: ['./workshop-create.component.css']
})
export class WorkshopCreateComponent {

  public createForm = this.formBuilder.group({  // Form group holding the values provided.
    title: "",
    description: "",
    host_first_name: "",
    host_last_name: "",
    host_description: "",
    location: "",
    time: "",
    requirements: "",
    spots: "",
  })

  workshopId: number

  constructor(
    protected workshopService: WorkshopService,
    protected formBuilder: FormBuilder,
    public dialogRef: MatDialogRef<WorkshopCreateComponent>,
    protected snackBar: MatSnackBar,
  ){
    let min = 100000;
    let max = 999999;
    this.workshopId = Math.floor(Math.random() * (max-min + 1) + min);
    this.createForm.get('title')?.addValidators(Validators.required);
    this.createForm.get('description')?.addValidators(Validators.required);
    this.createForm.get('host_first_name')?.addValidators(Validators.required);
    this.createForm.get('host_last_name')?.addValidators(Validators.required);
    this.createForm.get('host_description')?.addValidators(Validators.required);
    this.createForm.get('location')?.addValidators(Validators.required);
    this.createForm.get('time')?.addValidators(Validators.required);
    this.createForm.get('requirements')?.addValidators(Validators.required);
    this.createForm.get('spots')?.addValidators([Validators.required, Validators.pattern("^[0-9]*$"), Validators.min(0)]); // Validate values from the user given to the form.
  }


  onSubmit(): void { 
    let workshop: Workshop = {
      id: this.workshopId!,
      title: this.createForm.value.title!,
      description: this.createForm.value.description!,
      host_first_name: this.createForm.value.host_first_name!,
      host_last_name: this.createForm.value.host_last_name!,
      host_description: this.createForm.value.host_description!,
      location: this.createForm.value.location!,
      time: this.createForm.value.time!,
      requirements: this.createForm.value.requirements!,
      spots: parseInt(this.createForm.value.spots!),
      attendees: []
    }

    this.workshopService.createWorkshop(workshop).subscribe({
      next: () => this.onSuccess(),
    });
    this.dialogRef.close();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  private onSuccess() {
    this.snackBar.open("Workshop created!", "", { duration: 2000 })
  }
}
