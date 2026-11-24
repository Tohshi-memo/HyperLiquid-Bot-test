# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T05:37:28.373203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0546` n `13`; crypto_alt avg `0.2909` n `239`; crypto_major avg `0.1983` n `8`; equity avg `0.1445` n `166`; fx avg `0.0221` n `6`; index avg `0.0177` n `27`; metal avg `0.0233` n `20`; unknown avg `0.603` n `1264`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.6673` n `239`; crypto_major avg `0.26` n `8`; equity avg `0.1705` n `166`; fx avg `0.0348` n `6`; index avg `0.0256` n `27`; metal avg `0.0717` n `20`; unknown avg `0.1556` n `1254`
- 4h: commodity avg `-0.1179` n `13`; crypto_alt avg `0.3478` n `239`; crypto_major avg `-0.4358` n `8`; equity avg `-0.6725` n `166`; fx avg `-0.0059` n `6`; index avg `-0.023` n `27`; metal avg `-0.5219` n `20`; unknown avg `163.1517` n `1236`
- 24h: commodity avg `-1.3499` n `13`; crypto_alt avg `1.1566` n `239`; crypto_major avg `0.4112` n `8`; equity avg `4.682` n `166`; fx avg `-0.2284` n `6`; index avg `0.6639` n `27`; metal avg `-0.1174` n `20`; unknown avg `324.9868` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
