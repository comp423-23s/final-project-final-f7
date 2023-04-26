/* Component running behind the scenes of the webpage. 
Handles functionality of opening specific dialog boxes for different workshop-related tasks. */

import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';
import { MatDialog } from '@angular/material/dialog';
import { WorkshopRegisterComponent } from './workshop-register/workshop-register.component';
import { Profile, ProfileService } from '../profile/profile.service';
import { WorkshopCreateComponent } from './workshop-create/workshop-create.component';
import { WorkshopDeleteComponent } from './workshop-delete/workshop-delete.component';
import { PermissionService } from '../permission.service';
import { WorkshopEditComponent } from './workshop-edit/workshop-edit.component';

export interface WorkshopDialogData {  // Data to be passed to the dialog box components. Simply includes the workshop being referred to.
  workshop: Workshop
}

@Component({
  selector: 'app-workshop',
  templateUrl: './workshop.component.html',
  styleUrls: ['./workshop.component.css']
})
export class WorkshopComponent {

  public workshops$: Observable<Workshop[]>  // Holds all workshops obtained from the database.
  public profile$: Observable<Profile | undefined>  // Holds the currently logged in profile.
  public adminPermission$: Observable<boolean>  // Holds a boolean value indicating whether or not the current user has the administrator permission.

  public static Route = {
    path: 'workshops',
    component: WorkshopComponent,
    title: 'Workshops',
  }

  constructor(protected workshopService: WorkshopService, protected profileService: ProfileService, public dialog: MatDialog, private permission: PermissionService) {
    this.workshops$ = workshopService.getWorkshops();
    this.profile$ = profileService.profile$;
    this.adminPermission$ = this.permission.check('admin.view', 'admin/');
  }

  openRegisterDialog(workshop: Workshop): void {
    const dialogRef = this.dialog.open(WorkshopRegisterComponent, {
      data: {workshop: workshop}
    });
    dialogRef.afterClosed().subscribe(() => {
      this.workshops$ = this.workshopService.getWorkshops();
    });
  }

  openCreateDialog(): void {
    const dialogRef = this.dialog.open(WorkshopCreateComponent);
    dialogRef.afterClosed().subscribe(() => {
      this.workshops$ = this.workshopService.getWorkshops();
    });
  }  
  
  openDeleteDialog(workshop: Workshop): void{
    const dialogRef = this.dialog.open(WorkshopDeleteComponent, {
      data: {workshop: workshop}
    });
    dialogRef.afterClosed().subscribe(() => {
      this.workshops$ = this.workshopService.getWorkshops();
    });
  }

  openEditDialog(workshop: Workshop): void{
    const dialogRef = this.dialog.open(WorkshopEditComponent, {
      data: {workshop: workshop}
    });
    dialogRef.afterClosed().subscribe(() => {
      this.workshops$ = this.workshopService.getWorkshops();
    });
  }
}
