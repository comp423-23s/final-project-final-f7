/* Component running behind the scenes of the webpage. */

import { Component } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';
import { MatDialog } from '@angular/material/dialog';
import { WorkshopDialogComponent } from './workshop-dialog/workshop-dialog.component';
import { Profile, ProfileService } from '../profile/profile.service';

export interface WorkshopDialogData {
  workshop: Workshop
}

@Component({
  selector: 'app-workshop',
  templateUrl: './workshop.component.html',
  styleUrls: ['./workshop.component.css']
})
export class WorkshopComponent {

  // form = this.formBuilder.group({
  //   id: '',
  //   title: '',
  //   description: '',
  //   host_first_name: '',
  //   host_last_name: '',
  //   host_description: '',
  //   location: '',
  //   time: '',
  //   requirements: '',
  //   spots: '',
  //   attendees: '',
  // });


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

  openDialog(workshop: Workshop): void {
    this.dialog.open(WorkshopDialogComponent, {
      data: {workshop: workshop}
    });

    // dialogRef.afterClosed().subscribe(() => {
    //   this.workshops$ = this.workshopService.getWorkshops();
    // });
  }

}
