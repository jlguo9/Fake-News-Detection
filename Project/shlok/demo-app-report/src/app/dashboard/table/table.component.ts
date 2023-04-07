import { Component, OnInit } from '@angular/core';
import { SettingsService } from 'app/services/settings.service';
declare const $: any;


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
  description: string;
  showResults: Boolean = false;
  newsObj = {}

  modelFeedbackArr = {};

  results = [];
  //   {
  //     "model":"Model 1",
  //     "fake": 6
  //   },
  //   {
  //     "model":"Model 2",
  //     "fake": 70
  //   },
  //   {
  //     "model":"Model 3",
  //     "fake": 66
  //   },
  //   {
  //     "model":"Model 4",
  //     "fake": 55
  //   }
  // ]

  constructor(private settingsService: SettingsService) { }

  ngOnInit() {
    this.title = 'Minimum Wage increases in Canada';
    this.sourceLink = 'ircc.';
    this.description = " Alpha, beta, gamme, Minimum Wage increases in Canada"
    this.has_video = false;
    this.has_image = true;
  }

  evaluateArticle(){
    // this.showResults = !this.showResults;
    this.newsObj = {
      "title": this.title,
      "source": this.sourceLink,
      "has_image": this.has_image,
      "has_video": this.has_video,
      "description": this.description
    }

    this.settingsService.getModelResults(this.newsObj).subscribe((results:any[]) => {
      if(results.length>0){
        console.log(results);
        this.results = results;
        this.showResults = !this.showResults;

      }
    })


  }


  feedback(model, response){

    if(!this.modelFeedbackArr.hasOwnProperty(model.modelId)){
      
    this.settingsService.feedbackToModel(response, this.newsObj).subscribe(response => {

      this.showTooltip("primary", "Feedback Received. Thanks for the feedback!")
      this.modelFeedbackArr[model.modelId] = response;
    });
      
    }
    else{
      this.showTooltip("danger", "Feedback already Updated.")
    }

  }

  getTruthPercentage(prob){
    return 100 - prob//(Math.round((1-prob)*100)/100)*100;
  }
  getFakePercentage(prob){
    return prob;
  }

  showTooltip(color, text){
    let from = 'top';
    let align = 'right';
    let type = 'info';
      align = 'center';
      type = color;
    $.notify({
      message: text,
    }, {
      placement: {from, align},
      offset: {x: 20, y: 35},
      type,
      template: `<div class="alert alert-{0} alert-with-icon col-md-4">
          <i class="material-icons alert-icon">notifications</i>
          <button class="close" type="button" data-dismiss="alert" aria-label="Close"><i class="material-icons">close</i></button>
          <span>{2}</span>
        </div>`
    });
  }

}
