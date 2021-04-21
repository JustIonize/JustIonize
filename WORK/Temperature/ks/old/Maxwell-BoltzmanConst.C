{
    c1 = new TCanvas("c1","My", 1000, 1000);
    m = 0.497648;


    g2 = new TGraphErrors("ap_ks.txt");
    g2->SetMarkerStyle(7);
    gPad->SetLogy(1);    

    G2 = new TGraph("ap_ks.txt");
    G2->SetTitle("Maxwell-Boltzman + Const; X axis; Y axis");

    t = new TF1("t", "[1]*((x+[2])^2)*exp(-sqrt((x+[2])^2 + pow(m,2))*[0])",0, 6);
    G2->Fit(t);
    G2->Draw("APSAME");
    g2->Draw("P");
    
    t->SetLineWidth(3);
    t->SetLineColor(kRed+1);
    t->Draw("SAME");
}
