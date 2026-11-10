# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T22:07:28.394418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `0.2479` n `239`; crypto_major avg `0.1623` n `8`; equity avg `0.1348` n `160`; fx avg `-0.0038` n `6`; index avg `0.0034` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.1923` n `1252`
- 1h: commodity avg `-0.0071` n `13`; crypto_alt avg `0.2124` n `239`; crypto_major avg `0.0894` n `8`; equity avg `0.0654` n `160`; fx avg `-0.0021` n `6`; index avg `-0.0136` n `27`; metal avg `-0.0038` n `20`; unknown avg `0.561` n `1250`
- 4h: commodity avg `0.0565` n `13`; crypto_alt avg `0.6475` n `239`; crypto_major avg `1.2577` n `8`; equity avg `1.3792` n `160`; fx avg `0.0069` n `6`; index avg `0.1185` n `27`; metal avg `0.1164` n `20`; unknown avg `1.0786` n `1226`
- 24h: commodity avg `0.076` n `13`; crypto_alt avg `-0.8963` n `239`; crypto_major avg `-2.173` n `8`; equity avg `-1.311` n `160`; fx avg `-0.1039` n `6`; index avg `-0.1975` n `27`; metal avg `-0.6715` n `20`; unknown avg `20.4226` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2573`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
