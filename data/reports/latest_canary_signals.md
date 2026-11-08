# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T18:07:28.436621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0932` n `13`; crypto_alt avg `0.1457` n `239`; crypto_major avg `0.068` n `8`; equity avg `0.0361` n `158`; fx avg `-0.0032` n `6`; index avg `-0.008` n `27`; metal avg `-0.0033` n `20`; unknown avg `0.2697` n `1234`
- 1h: commodity avg `-0.0847` n `13`; crypto_alt avg `-0.0344` n `239`; crypto_major avg `-0.0699` n `8`; equity avg `0.0263` n `158`; fx avg `-0.0084` n `6`; index avg `-0.003` n `27`; metal avg `0.013` n `20`; unknown avg `0.5894` n `1226`
- 4h: commodity avg `-0.0782` n `13`; crypto_alt avg `-0.3635` n `239`; crypto_major avg `-0.2181` n `8`; equity avg `-0.0798` n `158`; fx avg `0.0384` n `6`; index avg `-0.0285` n `27`; metal avg `-0.0197` n `20`; unknown avg `0.0373` n `1202`
- 24h: commodity avg `0.0026` n `13`; crypto_alt avg `-2.1541` n `239`; crypto_major avg `-0.4585` n `8`; equity avg `0.1002` n `158`; fx avg `0.0737` n `6`; index avg `-0.0244` n `27`; metal avg `-0.0396` n `20`; unknown avg `12.1109` n `1056`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
