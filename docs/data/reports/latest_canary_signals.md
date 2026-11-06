# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T20:37:25.384160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0849` n `13`; crypto_alt avg `-0.0822` n `239`; crypto_major avg `0.0436` n `8`; equity avg `-0.0127` n `158`; fx avg `-0.0056` n `6`; index avg `-0.0063` n `27`; metal avg `0.026` n `20`; unknown avg `17.2752` n `1261`
- 1h: commodity avg `-0.0735` n `13`; crypto_alt avg `0.0497` n `239`; crypto_major avg `-0.0308` n `8`; equity avg `0.3729` n `158`; fx avg `-0.0098` n `6`; index avg `0.0055` n `27`; metal avg `0.0392` n `20`; unknown avg `45.6491` n `1235`
- 4h: commodity avg `0.124` n `13`; crypto_alt avg `-0.2673` n `239`; crypto_major avg `-0.2272` n `8`; equity avg `0.0263` n `158`; fx avg `-0.0183` n `6`; index avg `-0.0713` n `27`; metal avg `0.0182` n `20`; unknown avg `84.7092` n `1235`
- 24h: commodity avg `0.1418` n `13`; crypto_alt avg `0.8637` n `239`; crypto_major avg `-0.6601` n `8`; equity avg `2.3414` n `158`; fx avg `-0.1034` n `6`; index avg `0.284` n `27`; metal avg `-0.0742` n `20`; unknown avg `65.6282` n `1084`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
