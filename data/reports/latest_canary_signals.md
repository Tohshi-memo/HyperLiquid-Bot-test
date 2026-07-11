# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T21:07:24.578920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0301` n `230`; crypto_major avg `0.0975` n `8`; equity avg `0.0094` n `92`; fx avg `0.0032` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0732` n `765`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.1182` n `8`; equity avg `0.0338` n `92`; fx avg `0.0065` n `6`; index avg `-0.0094` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0287` n `765`
- 4h: commodity avg `0.0496` n `12`; crypto_alt avg `0.3489` n `230`; crypto_major avg `0.3836` n `8`; equity avg `0.1534` n `92`; fx avg `0.0216` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0043` n `765`
- 24h: commodity avg `-0.0069` n `12`; crypto_alt avg `1.2078` n `229`; crypto_major avg `1.0102` n `8`; equity avg `0.3915` n `92`; fx avg `0.0119` n `6`; index avg `0.014` n `25`; metal avg `-0.0501` n `20`; unknown avg `2.3205` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
