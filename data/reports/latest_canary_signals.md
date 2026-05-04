# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T02:00:27.601430+00:00`
- Correlation status: `ready`
- Asset price records: `223`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `7`; crypto_alt avg `0.7346` n `223`; crypto_major avg `1.0163` n `7`; equity avg `0.2385` n `42`; fx avg `0.0011` n `4`; index avg `0.1061` n `9`; metal avg `0.4313` n `7`; unknown avg `0.086` n `314`
- 1h: commodity avg `0.1302` n `7`; crypto_alt avg `0.9324` n `223`; crypto_major avg `1.4621` n `7`; equity avg `0.4834` n `42`; fx avg `0.0154` n `4`; index avg `0.3261` n `9`; metal avg `0.1755` n `7`; unknown avg `0.2786` n `314`
- 4h: commodity avg `0.7261` n `7`; crypto_alt avg `0.86` n `223`; crypto_major avg `1.3074` n `7`; equity avg `0.4336` n `42`; fx avg `0.0127` n `4`; index avg `0.171` n `9`; metal avg `0.0581` n `7`; unknown avg `0.2282` n `314`
- 24h: commodity avg `0.0094` n `7`; crypto_alt avg `1.5583` n `223`; crypto_major avg `2.0808` n `7`; equity avg `0.8049` n `42`; fx avg `0.0072` n `4`; index avg `0.5044` n `9`; metal avg `0.4241` n `7`; unknown avg `0.5705` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3794`, n `219`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3638`, n `219`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3475`, n `215`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3449`, n `215`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2467`, n `219`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2382`, n `219`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2197`, n `219`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1884`, n `219`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1753`, n `215`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1704`, n `219`, weak_sample_signal
