# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T23:52:25.008744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0356` n `230`; crypto_major avg `0.1117` n `8`; equity avg `0.0396` n `112`; fx avg `0.0094` n `6`; index avg `-0.0083` n `25`; metal avg `0.0282` n `20`; unknown avg `0.0276` n `782`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.0663` n `230`; crypto_major avg `-0.1332` n `8`; equity avg `0.0279` n `112`; fx avg `0.0009` n `6`; index avg `-0.0102` n `25`; metal avg `0.0765` n `20`; unknown avg `-0.1141` n `782`
- 4h: commodity avg `0.0859` n `12`; crypto_alt avg `-0.0119` n `230`; crypto_major avg `-0.1339` n `8`; equity avg `0.5495` n `112`; fx avg `-0.0006` n `6`; index avg `0.0225` n `25`; metal avg `0.03` n `20`; unknown avg `-0.1203` n `782`
- 24h: commodity avg `0.6473` n `12`; crypto_alt avg `0.0478` n `230`; crypto_major avg `-1.1397` n `8`; equity avg `0.6395` n `109`; fx avg `0.0298` n `6`; index avg `-0.1204` n `25`; metal avg `-0.1694` n `20`; unknown avg `112.7472` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
