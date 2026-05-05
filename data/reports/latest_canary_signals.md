# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T14:29:55.436945+00:00`
- Correlation status: `ready`
- Asset price records: `367`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `7`; crypto_alt avg `-0.058` n `223`; crypto_major avg `0.0456` n `7`; equity avg `0.8419` n `47`; fx avg `0.0136` n `4`; index avg `0.1537` n `6`; metal avg `0.049` n `7`; unknown avg `0.2714` n `312`
- 1h: commodity avg `-0.2607` n `7`; crypto_alt avg `-0.3897` n `223`; crypto_major avg `-0.3653` n `7`; equity avg `0.41` n `47`; fx avg `0.009` n `4`; index avg `0.2662` n `6`; metal avg `0.0611` n `7`; unknown avg `0.1504` n `312`
- 4h: commodity avg `-0.6457` n `7`; crypto_alt avg `0.3671` n `223`; crypto_major avg `0.8827` n `7`; equity avg `0.9614` n `47`; fx avg `0.0542` n `4`; index avg `0.625` n `6`; metal avg `0.3922` n `7`; unknown avg `0.5143` n `312`
- 24h: commodity avg `-0.1445` n `7`; crypto_alt avg `1.9164` n `223`; crypto_major avg `1.9534` n `7`; equity avg `0.6382` n `47`; fx avg `0.0816` n `4`; index avg `0.5717` n `6`; metal avg `0.3907` n `7`; unknown avg `0.3362` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `363`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2008`, n `363`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `363`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `363`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `363`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `363`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `363`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `363`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0958`, n `359`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `359`, weak_sample_signal
