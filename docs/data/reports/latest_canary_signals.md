# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T08:37:27.266080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0867` n `13`; crypto_alt avg `0.2727` n `239`; crypto_major avg `0.4133` n `8`; equity avg `-0.0776` n `162`; fx avg `0.0201` n `6`; index avg `-0.0083` n `27`; metal avg `0.0188` n `20`; unknown avg `0.4282` n `1262`
- 1h: commodity avg `0.0535` n `13`; crypto_alt avg `-0.486` n `239`; crypto_major avg `-0.2815` n `8`; equity avg `-0.3321` n `162`; fx avg `0.03` n `6`; index avg `-0.0241` n `27`; metal avg `-0.0649` n `20`; unknown avg `0.4617` n `1196`
- 4h: commodity avg `0.0282` n `13`; crypto_alt avg `1.8663` n `239`; crypto_major avg `1.0588` n `8`; equity avg `-0.4005` n `162`; fx avg `0.0714` n `6`; index avg `-0.0537` n `27`; metal avg `-0.239` n `20`; unknown avg `0.8838` n `1170`
- 24h: commodity avg `0.5377` n `13`; crypto_alt avg `-1.004` n `239`; crypto_major avg `-3.2389` n `8`; equity avg `-1.3436` n `162`; fx avg `-0.0162` n `6`; index avg `0.0169` n `27`; metal avg `-0.6034` n `20`; unknown avg `103.2576` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
