# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T06:38:01.907520+00:00`
- Correlation status: `ready`
- Asset price records: `336`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `7`; crypto_alt avg `-0.1193` n `223`; crypto_major avg `-0.0155` n `7`; equity avg `0.0223` n `47`; fx avg `-0.0034` n `4`; index avg `-0.0145` n `6`; metal avg `0.0434` n `7`; unknown avg `-0.0519` n `312`
- 1h: commodity avg `0.1802` n `7`; crypto_alt avg `-0.0778` n `223`; crypto_major avg `-0.0263` n `7`; equity avg `-0.0338` n `47`; fx avg `0.0147` n `4`; index avg `0.0358` n `6`; metal avg `0.0485` n `7`; unknown avg `-0.0737` n `310`
- 4h: commodity avg `0.1893` n `7`; crypto_alt avg `-0.0803` n `223`; crypto_major avg `0.5155` n `7`; equity avg `0.5998` n `47`; fx avg `-0.0038` n `4`; index avg `0.2512` n `6`; metal avg `0.0438` n `7`; unknown avg `1.2926` n `310`
- 24h: commodity avg `1.3333` n `7`; crypto_alt avg `0.9858` n `223`; crypto_major avg `0.6037` n `7`; equity avg `-0.238` n `47`; fx avg `-0.0302` n `4`; index avg `-0.1882` n `6`; metal avg `-1.3278` n `7`; unknown avg `0.6173` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2221`, n `332`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2154`, n `332`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `332`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `332`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1324`, n `332`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `332`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `332`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `332`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1044`, n `328`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `328`, weak_sample_signal
