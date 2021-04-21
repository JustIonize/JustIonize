//building and aprocsimation for ks_down

{
     g = new TGraph("ap_down_ks.txt");

    double x;
// fit function
    f = new TF1("f", "x*[0]", 0,5.5);
  //  f = new TF1("f", "[1]*2*pow((sqrt(pow(x,2)+pow(497.648*pow(10,6),2))/pi),0.5)*pow((8.61*[0]),-1.5)*exp(-sqrt(pow(x,2)+pow(497.648*pow(10,6),2))/(8.61*[0]))",0, 6);
    g->Fit(f);

    g->SetMarkerStyle(22);
    g->Draw("AP");
    //f->Draw("SAME");
}
