# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T14:22:30.659008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `13`; crypto_alt avg `-0.1387` n `239`; crypto_major avg `-0.3461` n `8`; equity avg `-0.1358` n `160`; fx avg `0.007` n `6`; index avg `-0.0021` n `27`; metal avg `0.01` n `20`; unknown avg `23.1166` n `1264`
- 1h: commodity avg `-0.132` n `13`; crypto_alt avg `-0.2012` n `239`; crypto_major avg `-0.9092` n `8`; equity avg `-0.9666` n `160`; fx avg `0.0139` n `6`; index avg `-0.0903` n `27`; metal avg `-0.087` n `20`; unknown avg `3.9394` n `1256`
- 4h: commodity avg `-0.0837` n `13`; crypto_alt avg `-0.056` n `239`; crypto_major avg `-1.0421` n `8`; equity avg `-1.8372` n `160`; fx avg `0.0134` n `6`; index avg `-0.128` n `27`; metal avg `-0.1701` n `20`; unknown avg `23.5472` n `1250`
- 24h: commodity avg `-0.5339` n `13`; crypto_alt avg `-0.5814` n `239`; crypto_major avg `-1.6618` n `8`; equity avg `1.4311` n `160`; fx avg `-0.0304` n `6`; index avg `0.2273` n `27`; metal avg `-0.3092` n `20`; unknown avg `2.4004` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
