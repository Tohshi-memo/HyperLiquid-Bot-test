# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T17:37:35.550166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `13`; crypto_alt avg `-0.0063` n `238`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0001` n `154`; fx avg `-0.0068` n `6`; index avg `0.0107` n `27`; metal avg `0.0204` n `20`; unknown avg `0.1906` n `1238`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.0087` n `238`; crypto_major avg `0.0713` n `8`; equity avg `-0.0599` n `154`; fx avg `-0.0003` n `6`; index avg `-0.0296` n `27`; metal avg `0.0255` n `20`; unknown avg `1.11` n `1234`
- 4h: commodity avg `-0.1969` n `13`; crypto_alt avg `0.9247` n `238`; crypto_major avg `0.8375` n `8`; equity avg `1.1649` n `154`; fx avg `-0.0209` n `6`; index avg `0.1727` n `27`; metal avg `0.2529` n `20`; unknown avg `1.0143` n `1150`
- 24h: commodity avg `-0.5788` n `13`; crypto_alt avg `0.2375` n `237`; crypto_major avg `0.7402` n `8`; equity avg `1.442` n `154`; fx avg `-0.0736` n `6`; index avg `0.3825` n `27`; metal avg `0.1239` n `20`; unknown avg `22.9258` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
