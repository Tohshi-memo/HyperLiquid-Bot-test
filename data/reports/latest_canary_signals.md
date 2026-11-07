# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T12:07:29.180322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.1038` n `239`; crypto_major avg `-0.0821` n `8`; equity avg `-0.0456` n `158`; fx avg `-0.0137` n `6`; index avg `-0.002` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.0026` n `1251`
- 1h: commodity avg `0.0114` n `13`; crypto_alt avg `-0.0844` n `239`; crypto_major avg `-0.1223` n `8`; equity avg `-0.0428` n `158`; fx avg `-0.0048` n `6`; index avg `-0.0134` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.1251` n `1249`
- 4h: commodity avg `0.074` n `13`; crypto_alt avg `-0.7543` n `239`; crypto_major avg `-0.3459` n `8`; equity avg `-0.0273` n `158`; fx avg `0.0039` n `6`; index avg `-0.0157` n `27`; metal avg `-0.0034` n `20`; unknown avg `134.763` n `1209`
- 24h: commodity avg `-0.0933` n `13`; crypto_alt avg `-1.4847` n `239`; crypto_major avg `-0.7937` n `8`; equity avg `-1.0151` n `158`; fx avg `-0.0502` n `6`; index avg `-0.0551` n `27`; metal avg `0.0308` n `20`; unknown avg `-0.4754` n `1113`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
