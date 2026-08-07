# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T10:22:31.953211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `-0.0211` n `8`; equity avg `-0.1226` n `112`; fx avg `-0.0032` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0823` n `20`; unknown avg `-0.0055` n `782`
- 1h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.1561` n `230`; crypto_major avg `0.1447` n `8`; equity avg `-0.1951` n `112`; fx avg `-0.0223` n `6`; index avg `-0.0361` n `25`; metal avg `-0.0732` n `20`; unknown avg `0.0596` n `782`
- 4h: commodity avg `-0.2329` n `12`; crypto_alt avg `0.0182` n `230`; crypto_major avg `0.6469` n `8`; equity avg `0.526` n `112`; fx avg `-0.0557` n `6`; index avg `0.0549` n `25`; metal avg `0.1306` n `20`; unknown avg `0.1124` n `782`
- 24h: commodity avg `0.255` n `12`; crypto_alt avg `0.6871` n `230`; crypto_major avg `0.2225` n `8`; equity avg `1.7452` n `109`; fx avg `-0.0871` n `6`; index avg `0.0102` n `25`; metal avg `0.253` n `20`; unknown avg `0.4508` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
