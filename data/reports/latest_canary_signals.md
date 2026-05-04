# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T07:45:27.363233+00:00`
- Correlation status: `ready`
- Asset price records: `246`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `7`; crypto_alt avg `-0.0006` n `223`; crypto_major avg `0.004` n `7`; equity avg `-0.0219` n `42`; fx avg `-0.0125` n `4`; index avg `-0.0408` n `9`; metal avg `-0.2587` n `7`; unknown avg `0.1879` n `314`
- 1h: commodity avg `0.0452` n `7`; crypto_alt avg `0.1127` n `223`; crypto_major avg `0.1381` n `7`; equity avg `0.1297` n `42`; fx avg `-0.0263` n `4`; index avg `-0.0964` n `9`; metal avg `-0.3592` n `7`; unknown avg `0.0915` n `314`
- 4h: commodity avg `0.2576` n `7`; crypto_alt avg `0.186` n `223`; crypto_major avg `-0.0658` n `7`; equity avg `-0.2716` n `42`; fx avg `0.0122` n `4`; index avg `0.1035` n `9`; metal avg `-0.9755` n `7`; unknown avg `-0.2319` n `312`
- 24h: commodity avg `0.4733` n `7`; crypto_alt avg `2.0746` n `223`; crypto_major avg `2.1537` n `7`; equity avg `1.1186` n `42`; fx avg `-0.0584` n `4`; index avg `0.8206` n `9`; metal avg `-0.6943` n `7`; unknown avg `-0.0633` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3673`, n `238`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3597`, n `238`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3495`, n `242`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3371`, n `242`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2023`, n `238`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.194`, n `238`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `242`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1715`, n `242`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1687`, n `242`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1612`, n `238`, weak_sample_signal
