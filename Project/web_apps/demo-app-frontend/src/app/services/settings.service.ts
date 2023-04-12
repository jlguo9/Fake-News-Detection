import { HttpClient } from '@angular/common/http';
import { Injectable, EventEmitter } from '@angular/core';

@Injectable()
export class SettingsService {
  public sidebarImageIndex = 4;
  public sidebarImageIndexUpdate: EventEmitter<number> = new EventEmitter();
  public sidebarFilter = '#fff';
  public sidebarFilterUpdate: EventEmitter<string> = new EventEmitter();
  public sidebarColor = '#D80B0B';
  public sidebarColorUpdate: EventEmitter<string> = new EventEmitter();

  // public backendUrl = "http://localhost:9090/"
  public backendUrl = "http://35.208.233.163:9090/"


  constructor(private http: HttpClient) { }

  getSidebarImageIndex(): number {
    return this.sidebarImageIndex;
  }
  setSidebarImageIndex(id) {
    this.sidebarImageIndex = id;
    this.sidebarImageIndexUpdate.emit(this.sidebarImageIndex);
  }
  getSidebarFilter(): string {
    return this.sidebarFilter;
  }
  setSidebarFilter(color: string) {
    this.sidebarFilter = color;
    this.sidebarFilterUpdate.emit(this.sidebarFilter);
  }
  getSidebarColor(): string {
    return this.sidebarColor;
  }
  setSidebarColor(color: string) {
    this.sidebarColor = color;
    this.sidebarColorUpdate.emit(this.sidebarColor);
  }


  getModelResults(newsInfo){
    // return this.http.get(this.backendUrl);
    return this.http.post(this.backendUrl + "evaluate-model", newsInfo);
  }

  feedbackToModel(feedback_value, newsObj){
    let feedBackObj = JSON.parse(JSON.stringify(newsObj));
    feedBackObj.feedback_value = feedback_value
    return this.http.post(this.backendUrl + "feedback", feedBackObj)
  }
}