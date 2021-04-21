{

    c1 = new TCanvas("c1","My", 1000, 1000);
    m = 0.497648;

   // TLatex text;
   // text.SetTextSize(0.25);
   // text.SetTextAlign(23);
   // text.DrawLatex(.2,.3,"p_{T} GeV");

    


    g1 = new TGraphErrors("ap_ks.txt");
    g1->SetMarkerStyle(7);
    gPad->SetLogy(1);

    G1 = new TGraph("ap_ks.txt");
    G1->SetTitle("Maxwell-Boltzman"); 

    f = new TF1("f", "[1]*((x)^2)*exp(-sqrt((x)^2 + pow(m,2))*[0])",0, 6);

    G1->Fit(f);
    G1->Draw("APSAME");
    g1->Draw("P");

    f->SetLineWidth(3);
    f->SetLineColor(kGreen+1);
    f->Draw("SAME");

}
