/* Component running behind the scenes of the webpage. */

import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';

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

  constructor(public workshopService: WorkshopService) {
    this.workshops$ = workshopService.getWorkshops();
  }
}