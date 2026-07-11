# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T06:07:24.592094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `-0.0047` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `0.0154` n `92`; fx avg `0.0` n `6`; index avg `-0.0022` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0167` n `733`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `0.0268` n `8`; equity avg `0.035` n `92`; fx avg `0.0234` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0031` n `733`
- 4h: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.1024` n `229`; crypto_major avg `0.1326` n `8`; equity avg `0.0931` n `92`; fx avg `0.0315` n `6`; index avg `0.0106` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0924` n `731`
- 24h: commodity avg `-0.3364` n `12`; crypto_alt avg `0.2639` n `229`; crypto_major avg `-0.3291` n `8`; equity avg `-0.32` n `92`; fx avg `-0.0492` n `6`; index avg `0.1079` n `25`; metal avg `-0.0009` n `20`; unknown avg `4.154` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
