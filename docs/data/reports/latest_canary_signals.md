# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T15:15:20.891274+00:00`
- Correlation status: `ready`
- Asset price records: `276`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0825` n `7`; crypto_alt avg `-0.0317` n `223`; crypto_major avg `-0.1569` n `7`; equity avg `0.1331` n `42`; fx avg `0.0019` n `4`; index avg `-0.0525` n `9`; metal avg `-0.1348` n `7`; unknown avg `-0.1194` n `314`
- 1h: commodity avg `0.5658` n `7`; crypto_alt avg `0.4726` n `223`; crypto_major avg `0.5449` n `7`; equity avg `0.1549` n `42`; fx avg `-0.0095` n `4`; index avg `0.0681` n `9`; metal avg `-0.4903` n `7`; unknown avg `-0.1119` n `314`
- 4h: commodity avg `0.2218` n `7`; crypto_alt avg `1.0039` n `223`; crypto_major avg `0.9719` n `7`; equity avg `0.913` n `42`; fx avg `0.0108` n `4`; index avg `0.62` n `9`; metal avg `0.0601` n `7`; unknown avg `-0.4885` n `314`
- 24h: commodity avg `1.4556` n `7`; crypto_alt avg `1.826` n `223`; crypto_major avg `1.4602` n `7`; equity avg `1.2037` n `42`; fx avg `-0.0768` n `4`; index avg `1.0885` n `9`; metal avg `-1.599` n `7`; unknown avg `-0.3691` n `311`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2583`, n `268`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2576`, n `272`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2547`, n `268`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2494`, n `272`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1544`, n `272`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `272`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1499`, n `272`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1471`, n `268`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `272`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1354`, n `268`, weak_sample_signal
