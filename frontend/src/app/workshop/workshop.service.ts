/* Service for handling workshop functionality on the frontend. 
Calls on underlying HTTP methods to handle backend functionality. */

import { Injectable } from '@angular/core';
import { Profile } from '../profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable, ObservedValueOf } from 'rxjs';

export interface Workshop {  // Interface representing a workshop object.
  id: number
  title: string
  description: string
  host_first_name: string
  host_last_name: string
  host_description: string
  location: string
  time: string
  requirements: string
  spots: number
  attendees: Profile[]
}

@Injectable({
  providedIn: 'root'
})
export class WorkshopService {

  constructor(private httpClient: HttpClient) { }

  getWorkshops(): Observable<Workshop[]> {
    return this.httpClient.get<Workshop[]>("/api/workshop");  // Calls underlying method from the workshop API to get all workshops.
  }

  createWorkshop(newWorkshop: Workshop): Observable<Workshop>{
    return this.httpClient.post<Workshop>("/api/workshop", newWorkshop);  // Calls underlying method from the workshop API to create a new workshop.
  }
    
  registerUser(profile: Profile, workshop: Workshop): Observable<Workshop> {
    return this.httpClient.put<Workshop>(`/api/workshop/${workshop.id}`, profile); // Calls underlying method from the workshop API to register a user.
  }

  checkRegister(workshop: Workshop): Observable<Profile[]> {
    return this.httpClient.get<Profile[]>(`/api/workshop/test/${workshop.id}`); // DO DOC
  }

  deleteWorkshop(workshop: Workshop){
    return this.httpClient.delete<null>(`/api/workshop/${workshop.id}`);  // Calls underlying method from the workshop API to delete a workshop.
  }
}
