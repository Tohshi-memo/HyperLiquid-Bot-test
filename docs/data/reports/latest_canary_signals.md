# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T05:37:44.379829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1206` n `13`; crypto_alt avg `0.1476` n `239`; crypto_major avg `0.1167` n `8`; equity avg `0.024` n `158`; fx avg `0.0069` n `6`; index avg `-0.0019` n `27`; metal avg `-0.137` n `20`; unknown avg `6.7625` n `1263`
- 1h: commodity avg `0.1234` n `13`; crypto_alt avg `-0.4056` n `239`; crypto_major avg `-0.1811` n `8`; equity avg `-0.3375` n `158`; fx avg `-0.0057` n `6`; index avg `-0.0622` n `27`; metal avg `-0.2065` n `20`; unknown avg `5.8022` n `1253`
- 4h: commodity avg `0.0251` n `13`; crypto_alt avg `0.0922` n `239`; crypto_major avg `0.0213` n `8`; equity avg `-0.2957` n `158`; fx avg `0.0121` n `6`; index avg `-0.0996` n `27`; metal avg `-0.0582` n `20`; unknown avg `0.2899` n `1232`
- 24h: commodity avg `-1.82` n `13`; crypto_alt avg `1.8674` n `239`; crypto_major avg `2.5877` n `8`; equity avg `-1.5247` n `158`; fx avg `0.1184` n `6`; index avg `-0.035` n `27`; metal avg `1.1337` n `20`; unknown avg `31.8945` n `1014`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2535`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
