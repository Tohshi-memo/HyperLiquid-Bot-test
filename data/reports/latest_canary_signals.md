# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T14:28:37.289623+00:00`
- Correlation status: `ready`
- Asset price records: `272`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `7`; crypto_alt avg `0.3523` n `223`; crypto_major avg `0.544` n `7`; equity avg `0.1653` n `42`; fx avg `0.0071` n `4`; index avg `0.181` n `9`; metal avg `0.1231` n `7`; unknown avg `-0.0525` n `314`
- 1h: commodity avg `0.2684` n `7`; crypto_alt avg `0.5095` n `223`; crypto_major avg `0.4334` n `7`; equity avg `0.7271` n `42`; fx avg `0.0128` n `4`; index avg `0.6263` n `9`; metal avg `0.3108` n `7`; unknown avg `-0.2953` n `314`
- 4h: commodity avg `-0.9368` n `7`; crypto_alt avg `0.8984` n `223`; crypto_major avg `0.833` n `7`; equity avg `1.4528` n `42`; fx avg `0.022` n `4`; index avg `0.8732` n `9`; metal avg `1.2653` n `7`; unknown avg `-0.1788` n `314`
- 24h: commodity avg `0.7462` n `7`; crypto_alt avg `1.508` n `223`; crypto_major avg `0.9077` n `7`; equity avg `1.1195` n `42`; fx avg `-0.0633` n `4`; index avg `1.0163` n `9`; metal avg `-1.0817` n `7`; unknown avg `-0.347` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.264`, n `268`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2557`, n `268`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.208`, n `264`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2066`, n `264`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `268`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1573`, n `268`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `268`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1537`, n `264`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1532`, n `264`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1527`, n `268`, weak_sample_signal
