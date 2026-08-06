# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T22:37:37.527196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `0.0691` n `8`; equity avg `-0.0544` n `112`; fx avg `-0.001` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.018` n `782`
- 1h: commodity avg `0.0923` n `12`; crypto_alt avg `0.1261` n `230`; crypto_major avg `0.0094` n `8`; equity avg `0.4511` n `112`; fx avg `-0.0009` n `6`; index avg `0.0175` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.1541` n `782`
- 4h: commodity avg `0.2532` n `12`; crypto_alt avg `-0.3152` n `230`; crypto_major avg `-0.3949` n `8`; equity avg `-0.674` n `112`; fx avg `0.0054` n `6`; index avg `-0.0803` n `25`; metal avg `-0.1061` n `20`; unknown avg `-0.2288` n `781`
- 24h: commodity avg `0.6244` n `12`; crypto_alt avg `0.2253` n `230`; crypto_major avg `-1.0234` n `8`; equity avg `0.2697` n `109`; fx avg `0.0262` n `6`; index avg `-0.2117` n `25`; metal avg `-0.1271` n `20`; unknown avg `113.2617` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
