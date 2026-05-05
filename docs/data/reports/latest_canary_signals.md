# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T09:30:29.301580+00:00`
- Correlation status: `ready`
- Asset price records: `348`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `7`; crypto_alt avg `0.1623` n `223`; crypto_major avg `-0.0463` n `7`; equity avg `0.1282` n `47`; fx avg `-0.0013` n `4`; index avg `-0.0448` n `6`; metal avg `-0.0638` n `7`; unknown avg `0.1845` n `312`
- 1h: commodity avg `0.0733` n `7`; crypto_alt avg `-0.0406` n `223`; crypto_major avg `-0.1934` n `7`; equity avg `0.0839` n `47`; fx avg `0.0264` n `4`; index avg `-0.1186` n `6`; metal avg `0.0816` n `7`; unknown avg `0.0056` n `312`
- 4h: commodity avg `-0.1289` n `7`; crypto_alt avg `0.3884` n `223`; crypto_major avg `-0.0356` n `7`; equity avg `0.2262` n `47`; fx avg `0.0621` n `4`; index avg `0.1258` n `6`; metal avg `0.4695` n `7`; unknown avg `0.3004` n `310`
- 24h: commodity avg `0.4939` n `7`; crypto_alt avg `1.1903` n `223`; crypto_major avg `0.5096` n `7`; equity avg `0.0554` n `47`; fx avg `0.0124` n `4`; index avg `0.0969` n `6`; metal avg `-0.1379` n `7`; unknown avg `-0.6299` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2177`, n `344`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2105`, n `344`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `344`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `344`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `344`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `344`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `344`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `344`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `340`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `340`, weak_sample_signal
