# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T00:07:31.019341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.3084` n `230`; crypto_major avg `0.1963` n `8`; equity avg `0.1519` n `112`; fx avg `0.0087` n `6`; index avg `0.0548` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.0129` n `782`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1982` n `230`; crypto_major avg `0.0527` n `8`; equity avg `0.2333` n `112`; fx avg `0.0158` n `6`; index avg `0.0504` n `25`; metal avg `0.0423` n `20`; unknown avg `-0.0744` n `782`
- 4h: commodity avg `0.0902` n `12`; crypto_alt avg `0.2963` n `230`; crypto_major avg `0.062` n `8`; equity avg `0.7007` n `112`; fx avg `0.0081` n `6`; index avg `0.0772` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.0963` n `782`
- 24h: commodity avg `0.6557` n `12`; crypto_alt avg `0.2678` n `230`; crypto_major avg `-0.9987` n `8`; equity avg `0.6922` n `109`; fx avg `0.0233` n `6`; index avg `-0.1062` n `25`; metal avg `-0.1628` n `20`; unknown avg `112.7608` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
