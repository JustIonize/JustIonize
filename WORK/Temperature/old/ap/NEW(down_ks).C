//building and aprocsimation for ks_down

{
     g = new TGraph("ap_down_ks.txt");

    double x;
// fit function
    f = new TF1("f", "pow(2*pi*497648000*8.61*[0],-1.5)*exp(-pow(x,2))/(2*497648000*8.61*[0])",0, 6);
    g->Fit(f);

    g->SetMarkerStyle(22);
    g->Draw("AP");
    f->Draw("SAME");
}
