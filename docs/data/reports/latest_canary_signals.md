# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T14:37:32.261880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.4636` n `239`; crypto_major avg `0.4382` n `8`; equity avg `0.7033` n `160`; fx avg `-0.0153` n `6`; index avg `0.042` n `27`; metal avg `-0.0841` n `20`; unknown avg `0.4576` n `1264`
- 1h: commodity avg `0.0034` n `13`; crypto_alt avg `0.5047` n `239`; crypto_major avg `-0.0217` n `8`; equity avg `0.5965` n `160`; fx avg `0.0074` n `6`; index avg `0.0347` n `27`; metal avg `-0.1188` n `20`; unknown avg `0.8437` n `1258`
- 4h: commodity avg `-0.1133` n `13`; crypto_alt avg `0.494` n `239`; crypto_major avg `-0.4644` n `8`; equity avg `-0.9605` n `160`; fx avg `-0.0193` n `6`; index avg `-0.0638` n `27`; metal avg `-0.2272` n `20`; unknown avg `20.1711` n `1250`
- 24h: commodity avg `-0.7936` n `13`; crypto_alt avg `-0.0838` n `239`; crypto_major avg `-1.2394` n `8`; equity avg `1.4029` n `160`; fx avg `-0.0499` n `6`; index avg `0.1569` n `27`; metal avg `-0.3191` n `20`; unknown avg `0.6618` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
