# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T08:00:35.073778+00:00`
- Correlation status: `ready`
- Asset price records: `247`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3196` n `7`; crypto_alt avg `-0.0825` n `223`; crypto_major avg `-0.1234` n `7`; equity avg `-0.0638` n `42`; fx avg `0.0008` n `4`; index avg `0.03` n `9`; metal avg `-0.1814` n `7`; unknown avg `0.5464` n `314`
- 1h: commodity avg `0.358` n `7`; crypto_alt avg `-0.0891` n `223`; crypto_major avg `0.0115` n `7`; equity avg `0.0596` n `42`; fx avg `-0.024` n `4`; index avg `-0.006` n `9`; metal avg `-0.5184` n `7`; unknown avg `0.4591` n `314`
- 4h: commodity avg `0.7666` n `7`; crypto_alt avg `-0.3278` n `223`; crypto_major avg `-0.5835` n `7`; equity avg `-0.4169` n `42`; fx avg `0.0062` n `4`; index avg `0.049` n `9`; metal avg `-1.1205` n `7`; unknown avg `-0.1127` n `312`
- 24h: commodity avg `0.7969` n `7`; crypto_alt avg `2.1834` n `223`; crypto_major avg `2.1202` n `7`; equity avg `1.0304` n `42`; fx avg `-0.0576` n `4`; index avg `0.8925` n `9`; metal avg `-0.8746` n `7`; unknown avg `0.1817` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3633`, n `239`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3559`, n `239`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3443`, n `243`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3324`, n `243`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2013`, n `239`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1933`, n `239`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `243`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.177`, n `243`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1715`, n `243`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `239`, weak_sample_signal
