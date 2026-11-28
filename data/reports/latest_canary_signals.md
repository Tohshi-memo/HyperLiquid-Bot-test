# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T21:22:36.299679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `13`; crypto_alt avg `-0.1934` n `239`; crypto_major avg `-0.1036` n `8`; equity avg `-0.0279` n `168`; fx avg `-0.0077` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0031` n `20`; unknown avg `4.3648` n `1260`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `-0.3465` n `239`; crypto_major avg `-0.1289` n `8`; equity avg `-0.0255` n `168`; fx avg `-0.0012` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0086` n `20`; unknown avg `5.2827` n `1208`
- 4h: commodity avg `0.1437` n `13`; crypto_alt avg `-0.2789` n `239`; crypto_major avg `-0.3186` n `8`; equity avg `0.1649` n `168`; fx avg `-0.0068` n `6`; index avg `0.0194` n `27`; metal avg `0.0059` n `20`; unknown avg `2731.4947` n `1176`
- 24h: commodity avg `0.0109` n `13`; crypto_alt avg `-3.5709` n `239`; crypto_major avg `-1.4369` n `8`; equity avg `-0.1725` n `168`; fx avg `-0.0123` n `6`; index avg `-0.0266` n `27`; metal avg `0.0182` n `20`; unknown avg `2.9025` n `1065`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
