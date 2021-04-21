#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "TLegend.h"

{
    c1 = new TCanvas("c1","My", 1500, 1000);
    double m = 0.497648;

    c1->cd();
    g5 = new TGraphErrors("ks_pp5.txt");
    g5->SetMarkerStyle(21);

    gPad->SetLogy(1);

    g5->SetTitle("1905_3; pT GeV ; d(sigma)/d(pT) mb*C/(GeV) ");

    
    k = new TF1("k", "[1]*x*pow((1-[2]*[0]*x),(1/[2]))",0, 6);
    k->SetParameter(2, -0.0736931);
    k->SetParameter(1, 296.137);
    k->SetParameter(0, 4.04043);


    g5->Fit(k,"NRM");
    g5->Draw("APSAME");


    

    k->SetLineWidth(3);
    k->SetLineColor(kGreen+1);
    k->Draw("SAME");

    g5->SetLineWidth(3);
    g5->Draw("PSAME");


    double temper5, t5e, chi5, ndf5;
    temper5 = k->GetParameter(0);
    t5e = k->GetParError(0);
    chi5 = k->GetChisquare();
    ndf5 = k->GetNDF();



 //   cout<<endl<<endl;
 //   cout<< "temperature 1 = "<<1/temper1<<endl;
 //   cout<< "t1 error = " <<t1e/(temper1*temper1)<<endl;
 //   cout<< "chi square = " << chi <<endl;
 //  cout<< "NDF = " << ndf <<endl<<endl;
}
