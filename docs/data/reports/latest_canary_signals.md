# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T18:37:29.788216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0503` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.0401` n `230`; crypto_major avg `-0.1984` n `8`; equity avg `-0.1018` n `112`; fx avg `0.0001` n `6`; index avg `-0.0141` n `25`; metal avg `0.0345` n `20`; unknown avg `-0.0228` n `782`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `0.0711` n `230`; crypto_major avg `0.1656` n `8`; equity avg `-0.0864` n `112`; fx avg `0.0138` n `6`; index avg `-0.0285` n `25`; metal avg `0.0547` n `20`; unknown avg `0.1123` n `782`
- 4h: commodity avg `0.0961` n `12`; crypto_alt avg `-0.3158` n `230`; crypto_major avg `-1.0417` n `8`; equity avg `0.2681` n `112`; fx avg `-0.0176` n `6`; index avg `0.0086` n `25`; metal avg `-0.0416` n `20`; unknown avg `-0.0267` n `782`
- 24h: commodity avg `0.3498` n `12`; crypto_alt avg `-0.5418` n `230`; crypto_major avg `-0.7568` n `8`; equity avg `0.4995` n `112`; fx avg `-0.1369` n `6`; index avg `-0.0758` n `25`; metal avg `0.3006` n `20`; unknown avg `-0.1234` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.293`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2745`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
