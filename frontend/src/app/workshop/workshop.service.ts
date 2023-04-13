/* Service for handling workshop functionality on the frontend. */

import { Injectable } from '@angular/core';
import { Profile } from '../profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Workshop {
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
    return this.httpClient.get<Workshop[]>("/api/workshop");  // Calls underlying method from the workshop API.
  }

  createWorkshop(newWorkshop: Workshop): Observable<Workshop>{
    return this.httpClient.post<Workshop>("/api/workshop", newWorkshop);
  }
    
  registerUser(profile: Profile, workshop: Workshop): Profile | null {
    for (let attendee of workshop.attendees) {
      if (attendee === profile) {
        return null;
      }
    }
    workshop.attendees.push(profile);
    workshop.spots--;
    this.httpClient.put<Workshop>("/api/workshop", [profile, workshop]);
    return profile;
  }

  delete_workshop(workshop: Workshop){
    return this.httpClient.delete<Workshop>(`/api/workshop/${workshop.id}`);
  }
}
