import { Component, Inject } from '@angular/core';
import { Workshop, WorkshopService } from '../workshop.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { WorkshopDialogData } from '../workshop.component';

@Component({
  selector: 'app-workshop-edit',
  templateUrl: './workshop-edit.component.html',
  styleUrls: ['./workshop-edit.component.css']
})

export class WorkshopEditComponent {

  public editForm = this.formBuilder.group({  // Form group holding the values provided.
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
    public dialogRef: MatDialogRef<WorkshopEditComponent>,
    protected snackBar: MatSnackBar,
    @Inject(MAT_DIALOG_DATA) public workshopDialogData: WorkshopDialogData

  ){
    this.editForm.get('title')?.addValidators(Validators.required);
    this.editForm.get('description')?.addValidators(Validators.required);
    this.editForm.get('host_first_name')?.addValidators(Validators.required);
    this.editForm.get('host_last_name')?.addValidators(Validators.required);
    this.editForm.get('host_description')?.addValidators(Validators.required);
    this.editForm.get('location')?.addValidators(Validators.required);
    this.editForm.get('time')?.addValidators(Validators.required);
    this.editForm.get('requirements')?.addValidators(Validators.required);
    this.editForm.get('spots')?.addValidators(Validators.required);
  }

  ngOnInit(): void{
    let workshop = this.workshopDialogData.workshop
    this.editForm.setValue({
      title: workshop.title,
      description: workshop.description,
      host_first_name: workshop.host_first_name,
      host_last_name: workshop.host_last_name,
      host_description: workshop.host_description,
      location: workshop.location,
      time: workshop.time,
      requirements: workshop.requirements,
      spots: "" + workshop.spots
    })
  }

  onSubmit(): void{
    let workshop = this.workshopDialogData.workshop
    let newWorkshop: Workshop ={
      id: workshop.id,
      title: this.editForm.value.title!,
      description: this.editForm.value.description!,
      host_first_name: this.editForm.value.host_first_name!,
      host_last_name: this.editForm.value.host_last_name!,
      host_description: this.editForm.value.host_description!,
      location: this.editForm.value.location!,
      time: this.editForm.value.time!,
      requirements: this.editForm.value.requirements!,
      spots: parseInt(this.editForm.value.spots!),
      attendees: workshop.attendees
    }
    this.workshopService.updateWorkshop(newWorkshop).subscribe({
      next: (newWorkshop) => this.onSuccess(newWorkshop),
      error: (err) => this.onError(err)
    });
    this.dialogRef.close();
  }

  private onSuccess(workshop: Workshop){
    this.snackBar.open(`${workshop.title} Updated!`,"", {duration: 2000})
  }

  private onError(error: any){
    //todo
  }
  onNoClick(): void{
    this.dialogRef.close();
  }
}
