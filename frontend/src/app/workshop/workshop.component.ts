/* Component running behind the scenes of the webpage. */

import { Component } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';
import { Workshop, WorkshopService } from './workshop.service';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-workshop',
  templateUrl: './workshop.component.html',
  styleUrls: ['./workshop.component.css']
})
export class WorkshopComponent {

  form = this.formBuilder.group({
    id: '',
    title: '',
    description: '',
    host_first_name: '',
    host_last_name: '',
    host_description: '',
    location: '',
    time: '',
    requirements: '',
    spots: '',
    attendees: '',
  });


  public workshops$: Observable<Workshop[]>  // Holds all workshops obtained from the database.

  public static Route = {
    path: 'workshops',
    component: WorkshopComponent,
    title: 'Workshops',
  }

  constructor(public workshopService: WorkshopService, private formBuilder: FormBuilder) {
    this.workshops$ = workshopService.getWorkshops();
  }

  onSubmit(): void {
    let form = this.form.value;
    let id = parseInt(form.id ?? "");
    let title = form.title ?? "";
    let description = form.description ?? "";
    let host_first_name = form.host_first_name ?? "";
    let host_last_name = form.host_last_name ?? "";
    let host_description = form.host_description ?? "";
    let location = form.location ?? "";
    let time = form.time ?? "";
    let requirements = form.requirements ?? "";
    let spots = parseInt(form.spots ?? "");
    let attendees = form.attendees ?? "";

    


    // let new_workshop = new Observable<Workshop>;
    // new_workshop.
    // this.workshops$.pipe(new_workshop);
    // this.workshopService.getWorkshops

    // this.workshopService.createWorkshop(id, title, description, host_first_name, host_last_name, host_description, location, time, requirements, spots, attendees, Workshop)
  }
}