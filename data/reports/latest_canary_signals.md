# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T14:15:58.704761+00:00`
- Correlation status: `ready`
- Asset price records: `272`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `7`; crypto_alt avg `0.1091` n `223`; crypto_major avg `0.2073` n `7`; equity avg `-0.0974` n `42`; fx avg `0.0071` n `4`; index avg `0.2497` n `9`; metal avg `-0.0465` n `7`; unknown avg `0.0029` n `314`
- 1h: commodity avg `0.2362` n `7`; crypto_alt avg `0.2643` n `223`; crypto_major avg `0.0972` n `7`; equity avg `0.4643` n `42`; fx avg `0.0127` n `4`; index avg `0.6963` n `9`; metal avg `0.1408` n `7`; unknown avg `-0.4584` n `314`
- 4h: commodity avg `-0.9686` n `7`; crypto_alt avg `0.6494` n `223`; crypto_major avg `0.4953` n `7`; equity avg `1.1877` n `42`; fx avg `0.022` n `4`; index avg `0.9432` n `9`; metal avg `1.0934` n `7`; unknown avg `-0.3382` n `314`
- 24h: commodity avg `0.7134` n `7`; crypto_alt avg `1.2495` n `223`; crypto_major avg `0.5698` n `7`; equity avg `0.8521` n `42`; fx avg `-0.0633` n `4`; index avg `1.0871` n `9`; metal avg `-1.2488` n `7`; unknown avg `-0.4827` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2652`, n `268`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2569`, n `268`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2096`, n `264`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2081`, n `264`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `268`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `268`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1589`, n `264`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1567`, n `264`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1555`, n `268`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.154`, n `268`, weak_sample_signal
