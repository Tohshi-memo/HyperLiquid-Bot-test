# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T18:07:30.254230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `0.0223` n `239`; crypto_major avg `-0.0067` n `8`; equity avg `-0.0125` n `168`; fx avg `0.0011` n `6`; index avg `0.002` n `27`; metal avg `0.0035` n `20`; unknown avg `1.3112` n `1244`
- 1h: commodity avg `-0.0204` n `13`; crypto_alt avg `-0.5232` n `239`; crypto_major avg `-0.5603` n `8`; equity avg `-0.0918` n `168`; fx avg `-0.013` n `6`; index avg `-0.005` n `27`; metal avg `-0.0173` n `20`; unknown avg `-0.072` n `1235`
- 4h: commodity avg `-0.071` n `13`; crypto_alt avg `-0.7383` n `239`; crypto_major avg `0.0408` n `8`; equity avg `0.0594` n `168`; fx avg `0.0124` n `6`; index avg `0.0061` n `27`; metal avg `-0.0098` n `20`; unknown avg `42.5011` n `1207`
- 24h: commodity avg `-0.1205` n `13`; crypto_alt avg `-3.4114` n `239`; crypto_major avg `-1.5306` n `8`; equity avg `-0.526` n `168`; fx avg `-0.0096` n `6`; index avg `-0.0436` n `27`; metal avg `0.111` n `20`; unknown avg `196.4365` n `1052`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
