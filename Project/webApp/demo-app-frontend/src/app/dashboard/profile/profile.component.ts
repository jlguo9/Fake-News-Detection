import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  firstName: string;
  lastName: string;
  menuItem = {path:"demo"}

  constructor(private router: ActivatedRoute) { }

  ngOnInit() {
    this.firstName = 'Alec';
    this.lastName = 'Thompson';
  }

  openDemo(){
    // this.router.(['/details/1029']);
  }



}
