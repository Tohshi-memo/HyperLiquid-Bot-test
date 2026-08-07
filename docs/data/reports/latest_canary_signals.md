# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T01:22:27.095641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.0788` n `230`; crypto_major avg `-0.0846` n `8`; equity avg `-0.5612` n `112`; fx avg `-0.0145` n `6`; index avg `-0.1284` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.2213` n `782`
- 1h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.1774` n `230`; crypto_major avg `0.1143` n `8`; equity avg `-0.3729` n `112`; fx avg `-0.0369` n `6`; index avg `-0.0952` n `25`; metal avg `0.0368` n `20`; unknown avg `0.064` n `782`
- 4h: commodity avg `0.0498` n `12`; crypto_alt avg `0.3426` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `-0.1855` n `112`; fx avg `-0.04` n `6`; index avg `-0.1441` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0088` n `782`
- 24h: commodity avg `0.4497` n `12`; crypto_alt avg `0.3621` n `230`; crypto_major avg `-0.8984` n `8`; equity avg `0.68` n `109`; fx avg `0.0446` n `6`; index avg `-0.1179` n `25`; metal avg `-0.1888` n `20`; unknown avg `113.1059` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
