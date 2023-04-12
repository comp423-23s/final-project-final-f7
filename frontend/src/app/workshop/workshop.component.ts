/* Component running behind the scenes of the webpage. */

import { Component } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';
import { MatDialog } from '@angular/material/dialog';
import { WorkshopDialogComponent } from './workshop-dialog/workshop-dialog.component';
import { Profile, ProfileService } from '../profile/profile.service';
import { WorkshopCreateComponent } from './workshop-create/workshop-create.component';
import { WorkshopDeleteComponent } from './workshop-delete/workshop-delete.component';

export interface WorkshopDialogData {
  workshop: Workshop
}

@Component({
  selector: 'app-workshop',
  templateUrl: './workshop.component.html',
  styleUrls: ['./workshop.component.css']
})
export class WorkshopComponent {

  public workshops$: Observable<Workshop[]>  // Holds all workshops obtained from the database.
  public profile$: Observable<Profile | undefined>

  public static Route = {
    path: 'workshops',
    component: WorkshopComponent,
    title: 'Workshops',
  }

  constructor(protected workshopService: WorkshopService, protected profileService: ProfileService, public dialog: MatDialog) {
    this.workshops$ = workshopService.getWorkshops();
    this.profile$ = profileService.profile$;
  }

  openRegisterDialog(workshop: Workshop): void {
    const dialogRef = this.dialog.open(WorkshopDialogComponent, {
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
}
