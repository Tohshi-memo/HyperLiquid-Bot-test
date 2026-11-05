# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T01:07:31.172855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `-0.2343` n `239`; crypto_major avg `-0.3124` n `8`; equity avg `-0.267` n `158`; fx avg `-0.0137` n `6`; index avg `-0.0493` n `27`; metal avg `-0.0373` n `20`; unknown avg `0.1186` n `1258`
- 1h: commodity avg `-0.086` n `13`; crypto_alt avg `0.015` n `239`; crypto_major avg `0.0581` n `8`; equity avg `-0.4281` n `158`; fx avg `-0.0449` n `6`; index avg `-0.0961` n `27`; metal avg `0.1612` n `20`; unknown avg `0.3658` n `1258`
- 4h: commodity avg `-0.1659` n `13`; crypto_alt avg `0.2049` n `239`; crypto_major avg `0.2934` n `8`; equity avg `-0.6996` n `158`; fx avg `-0.0369` n `6`; index avg `-0.1717` n `27`; metal avg `0.119` n `20`; unknown avg `-0.2738` n `1196`
- 24h: commodity avg `-1.9612` n `13`; crypto_alt avg `2.9634` n `239`; crypto_major avg `3.5099` n `8`; equity avg `-0.4988` n `158`; fx avg `-0.0143` n `6`; index avg `0.1949` n `27`; metal avg `1.5105` n `20`; unknown avg `30.2656` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2647`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
