# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T10:52:28.219719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1581` n `13`; crypto_alt avg `-0.0123` n `239`; crypto_major avg `-0.0216` n `8`; equity avg `-0.2603` n `160`; fx avg `-0.0044` n `6`; index avg `-0.0137` n `27`; metal avg `-0.0119` n `20`; unknown avg `0.7737` n `1262`
- 1h: commodity avg `0.287` n `13`; crypto_alt avg `-0.4356` n `239`; crypto_major avg `-0.5553` n `8`; equity avg `-0.7653` n `160`; fx avg `0.0197` n `6`; index avg `-0.0718` n `27`; metal avg `-0.0466` n `20`; unknown avg `0.2576` n `1256`
- 4h: commodity avg `-0.0824` n `13`; crypto_alt avg `-0.6553` n `239`; crypto_major avg `-1.0044` n `8`; equity avg `-0.3863` n `160`; fx avg `0.0137` n `6`; index avg `-0.058` n `27`; metal avg `-0.2527` n `20`; unknown avg `19.246` n `1219`
- 24h: commodity avg `-0.6318` n `13`; crypto_alt avg `0.8586` n `239`; crypto_major avg `0.0215` n `8`; equity avg `3.8853` n `160`; fx avg `-0.0585` n `6`; index avg `0.4276` n `27`; metal avg `0.0084` n `20`; unknown avg `5.281` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
