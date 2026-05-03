# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T23:00:27.919590+00:00`
- Correlation status: `ready`
- Asset price records: `211`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1186` n `7`; crypto_alt avg `-0.1669` n `223`; crypto_major avg `-0.1529` n `7`; equity avg `-0.1298` n `42`; fx avg `-0.004` n `4`; index avg `-0.0204` n `9`; metal avg `-0.1413` n `7`; unknown avg `0.0168` n `314`
- 1h: commodity avg `0.4838` n `7`; crypto_alt avg `0.2799` n `223`; crypto_major avg `0.4805` n `7`; equity avg `-0.1104` n `42`; fx avg `-0.0064` n `4`; index avg `-0.2827` n `9`; metal avg `0.0612` n `7`; unknown avg `0.0227` n `314`
- 4h: commodity avg `-0.1403` n `7`; crypto_alt avg `0.2912` n `223`; crypto_major avg `0.5568` n `7`; equity avg `0.0587` n `42`; fx avg `-0.0276` n `4`; index avg `-0.0189` n `9`; metal avg `0.0155` n `7`; unknown avg `0.1006` n `314`
- 24h: commodity avg `-0.1986` n `7`; crypto_alt avg `0.0397` n `223`; crypto_major avg `0.5953` n `7`; equity avg `0.2003` n `42`; fx avg `-0.0193` n `4`; index avg `0.0522` n `9`; metal avg `0.4242` n `7`; unknown avg `0.2223` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3917`, n `207`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3744`, n `207`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3178`, n `207`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3134`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3073`, n `207`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2956`, n `203`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2953`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2948`, n `203`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2947`, n `207`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2345`, n `207`, weak_sample_signal
