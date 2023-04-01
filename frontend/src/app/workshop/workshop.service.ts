import { Injectable } from '@angular/core';
import { Profile } from '../profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Workshop {
  id: number
  title: string
  description: string
  location: string
  time: string
  requirements: string
  spots: number
  hosts: Profile[]
  attendees: Profile[]
}

@Injectable({
  providedIn: 'root'
})
export class WorkshopService {

  constructor(private httpClient: HttpClient) { }

  getWorkshops(): Observable<Workshop[]> {
    return this.httpClient.get<Workshop[]>("/api/workshop");
  }
}
