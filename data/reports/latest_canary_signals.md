# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T12:15:39.727275+00:00`
- Correlation status: `ready`
- Asset price records: `264`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1706` n `7`; crypto_alt avg `0.0229` n `223`; crypto_major avg `0.0335` n `7`; equity avg `-0.0075` n `42`; fx avg `0.0054` n `4`; index avg `0.0361` n `9`; metal avg `0.1411` n `7`; unknown avg `-0.0321` n `314`
- 1h: commodity avg `-0.3714` n `7`; crypto_alt avg `0.0276` n `223`; crypto_major avg `-0.0713` n `7`; equity avg `0.0843` n `42`; fx avg `0.0003` n `4`; index avg `0.0263` n `9`; metal avg `-0.0039` n `7`; unknown avg `-0.2572` n `314`
- 4h: commodity avg `-0.2606` n `7`; crypto_alt avg `-0.9325` n `223`; crypto_major avg `-1.2088` n `7`; equity avg `-0.4526` n `42`; fx avg `0.0004` n `4`; index avg `-0.2692` n `9`; metal avg `-0.5741` n `7`; unknown avg `-0.5417` n `314`
- 24h: commodity avg `0.6319` n `7`; crypto_alt avg `0.798` n `223`; crypto_major avg `0.3194` n `7`; equity avg `0.406` n `42`; fx avg `-0.0737` n `4`; index avg `0.4628` n `9`; metal avg `-1.5816` n `7`; unknown avg `-0.0384` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2803`, n `260`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2726`, n `260`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1842`, n `260`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1811`, n `256`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1712`, n `260`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1709`, n `256`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1701`, n `256`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1685`, n `256`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1631`, n `260`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1605`, n `256`, weak_sample_signal
