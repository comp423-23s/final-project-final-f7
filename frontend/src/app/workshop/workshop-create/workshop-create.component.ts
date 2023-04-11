import { Component, Inject } from '@angular/core';
import { Workshop, WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { WorkshopDialogData } from '../workshop.component';
import { FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-workshop-create',
  templateUrl: './workshop-create.component.html',
  styleUrls: ['./workshop-create.component.css']
})
export class WorkshopCreateComponent {

  public workshop: Workshop | undefined

  public createForm = this.formBuilder.group({
    id: "",
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

  constructor(
    protected workshopService: WorkshopService,
    protected formBuilder: FormBuilder,
    public dialogRef: MatDialogRef<WorkshopCreateComponent>,
  ){
    this.createForm.get('id')?.addValidators(Validators.required);
    this.createForm.get('title')?.addValidators(Validators.required);
    this.createForm.get('description')?.addValidators(Validators.required);
    this.createForm.get('host_first_name')?.addValidators(Validators.required);
    this.createForm.get('host_last_name')?.addValidators(Validators.required);
    this.createForm.get('host_description')?.addValidators(Validators.required);
    this.createForm.get('location')?.addValidators(Validators.required);
    this.createForm.get('time')?.addValidators(Validators.required);
    this.createForm.get('requirements')?.addValidators(Validators.required);
    this.createForm.get('spots')?.addValidators(Validators.required);
  }
  
  onSubmit(): void {
    let workshop: Workshop = {
      id: parseInt(this.createForm.value.id!),
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

    this.workshopService.createWorkshop(workshop);
    this.dialogRef.close();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
}