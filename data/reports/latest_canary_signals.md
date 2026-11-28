# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T19:22:34.477532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.0334` n `239`; crypto_major avg `-0.1021` n `8`; equity avg `-0.0099` n `168`; fx avg `-0.0168` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0002` n `20`; unknown avg `1.1215` n `1266`
- 1h: commodity avg `0.1265` n `13`; crypto_alt avg `0.0469` n `239`; crypto_major avg `0.0237` n `8`; equity avg `0.123` n `168`; fx avg `0.0031` n `6`; index avg `0.0154` n `27`; metal avg `0.0152` n `20`; unknown avg `1.2825` n `1258`
- 4h: commodity avg `0.075` n `13`; crypto_alt avg `-0.6719` n `239`; crypto_major avg `-0.2758` n `8`; equity avg `0.0366` n `168`; fx avg `-0.0038` n `6`; index avg `0.0074` n `27`; metal avg `0.0064` n `20`; unknown avg `206.9385` n `1211`
- 24h: commodity avg `-0.0084` n `13`; crypto_alt avg `-3.2626` n `239`; crypto_major avg `-1.5014` n `8`; equity avg `-0.1429` n `168`; fx avg `-0.0095` n `6`; index avg `-0.0203` n `27`; metal avg `0.18` n `20`; unknown avg `-0.249` n `1069`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
