#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    double m = 0.497648;

    c1->cd(4);
    g4 = new TGraphErrors("ks_pp5.txt");
    g4->SetMarkerStyle(21);

    gPad->SetLogy(1);

   g4->SetTitle("1905_2; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    j = new TF1("j", "[1]*x*pow((1-[2]*[0]*(pow((x*x+0.497648*0.497648),0.5))),(1/[2]))",0, 6);
    j->SetParameter(2, 0.001);
    j->SetParameter(1, 100);
    j->SetParameter(0, 5);


    g4->Fit(j,"NRM");
    g4->Draw("APSAME");

    

    j->SetLineWidth(3);
    j->SetLineColor(kGreen+1);
    j->Draw("SAME");

    g4->SetLineWidth(3);
    g4->Draw("PSAME");


    double temper4, t4e, chi4, ndf4;
    temper4 = j->GetParameter(0);
    t4e = j->GetParError(0);
    chi4 = j->GetChisquare();
    ndf4 = j->GetNDF();



 //   cout<<endl<<endl;
 //   cout<< "temperature 1 = "<<1/temper1<<endl;
 //   cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
 //   cout<< "chi square = " << chi <<endl;
 //   cout<< "NDF = " << ndf <<endl<<endl;
}
