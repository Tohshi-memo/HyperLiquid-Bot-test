# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T10:07:35.188929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0724` n `13`; crypto_alt avg `-0.2907` n `239`; crypto_major avg `-0.1914` n `8`; equity avg `-0.1051` n `160`; fx avg `0.0104` n `6`; index avg `-0.0224` n `27`; metal avg `0.0119` n `20`; unknown avg `-0.0647` n `1258`
- 1h: commodity avg `-0.1432` n `13`; crypto_alt avg `-0.0781` n `239`; crypto_major avg `0.0256` n `8`; equity avg `0.3308` n `160`; fx avg `-0.029` n `6`; index avg `0.0177` n `27`; metal avg `-0.0394` n `20`; unknown avg `33.084` n `1254`
- 4h: commodity avg `-0.4037` n `13`; crypto_alt avg `-0.1662` n `239`; crypto_major avg `-0.5906` n `8`; equity avg `0.0907` n `160`; fx avg `-0.0047` n `6`; index avg `-0.0275` n `27`; metal avg `-0.2709` n `20`; unknown avg `19.6359` n `1217`
- 24h: commodity avg `-1.0296` n `13`; crypto_alt avg `1.0204` n `239`; crypto_major avg `0.3406` n `8`; equity avg `4.522` n `160`; fx avg `-0.0641` n `6`; index avg `0.4785` n `27`; metal avg `0.048` n `20`; unknown avg `5.3399` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
