import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  title: string;
  sourceLink: string;
  has_video: Boolean;
  has_image: Boolean;
  showResults: Boolean = false;

  results = [
    {
      "model":"Model 1",
      "fake": 6
    },
    {
      "model":"Model 2",
      "fake": 70
    },
    {
      "model":"Model 3",
      "fake": 66
    },
    {
      "model":"Model 4",
      "fake": 55
    }
  ]

  constructor() { }

  ngOnInit() {
    this.title = 'Minimum Wage increases in Canada';
    this.sourceLink = 'ircc.';

    this.has_video = false;
    this.has_image = true;
  }

  evaluateArticle(){
    this.showResults = !this.showResults;
  }

  getTruthPercentage(prob){
    return 100 - prob//(Math.round((1-prob)*100)/100)*100;
  }
  getFakePercentage(prob){
    return prob;
  }

}
