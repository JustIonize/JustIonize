#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    double m = 0.497648;

    c1->cd();
    g6 = new TGraphErrors("ks_pp5.txt");
    g6->SetMarkerStyle(21);

    gPad->SetLogy(1);
    g6->SetTitle("Andronic; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    l = new TF1("l", "[1]*x*pow((1+pow((x*[0]),2)),(-[2]))",0, 6);
//    f->SetParameter(2, 6);
//    f->SetParameter(1, 1000);
//    f->SetParameter(0, 5.8);

//    f->SetParameter(2, 4);
//    f->SetParameter(1, 10000);
//    f->SetParameter(0, 11.6);

    l->SetParameter(2, 4);
    l->SetParameter(1, 1000000);
    l->SetParameter(0, 5);


    g6->Fit(l,"NRM");
    g6->Draw("APSAME");
//    g6->Fit(f,"NRM");
//    g6->Draw("APSAME");
    

    l->SetLineWidth(3);
    l->SetLineColor(kGreen+1);
    l->Draw("SAME");

    g6->SetLineWidth(3);
    g6->Draw("PSAME");


    double temper6, t6e, chi6, ndf6;
    temper6 = l->GetParameter(0);
    t6e = l->GetParError(0);
    chi6 = l->GetChisquare();
    ndf6 = l->GetNDF();



//    cout<<endl<<endl;
 //   cout<< "temperature 1 = "<<1/temper1<<endl;
//    cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
//    cout<< "chi square = " << chi <<endl;
//    cout<< "NDF = " << ndf <<endl<<endl;   
}
