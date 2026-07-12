# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T03:07:24.859609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `-0.0099` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `0.0124` n `92`; fx avg `0.0025` n `6`; index avg `-0.0054` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0373` n `765`
- 1h: commodity avg `-0.0614` n `12`; crypto_alt avg `0.0355` n `230`; crypto_major avg `-0.0126` n `8`; equity avg `0.0161` n `92`; fx avg `0.0007` n `6`; index avg `-0.0145` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0646` n `765`
- 4h: commodity avg `0.2448` n `12`; crypto_alt avg `-0.7724` n `230`; crypto_major avg `-0.9143` n `8`; equity avg `-0.0901` n `92`; fx avg `0.0116` n `6`; index avg `-0.096` n `25`; metal avg `-0.0386` n `20`; unknown avg `0.3782` n `765`
- 24h: commodity avg `0.4889` n `12`; crypto_alt avg `-0.7534` n `229`; crypto_major avg `-0.3905` n `8`; equity avg `0.0381` n `92`; fx avg `0.0205` n `6`; index avg `-0.0994` n `25`; metal avg `-0.073` n `20`; unknown avg `0.0863` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
