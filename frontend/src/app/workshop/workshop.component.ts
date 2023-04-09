/* Component running behind the scenes of the webpage. */

import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';
import { MatDialog } from '@angular/material/dialog';
import { WorkshopDialogComponent } from './workshop-dialog/workshop-dialog.component';

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

  public static Route = {
    path: 'workshops',
    component: WorkshopComponent,
    title: 'Workshops',
  }

  constructor(protected workshopService: WorkshopService, public dialog: MatDialog) {
    this.workshops$ = workshopService.getWorkshops();
  }

  openDialog(workshop: Workshop): void {
    const dialogRef = this.dialog.open(WorkshopDialogComponent, {
      data: {workshop: workshop}
    });

    dialogRef.afterClosed().subscribe(() => {
      this.workshops$ = this.workshopService.getWorkshops();
    });
  }

}
