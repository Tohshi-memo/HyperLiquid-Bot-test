# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T01:15:18.201413+00:00`
- Correlation status: `ready`
- Asset price records: `28`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `7`; crypto_alt avg `0.1274` n `223`; crypto_major avg `0.1029` n `7`; equity avg `0.0091` n `42`; fx avg `0.0` n `4`; index avg `0.0512` n `9`; metal avg `-0.0013` n `7`; unknown avg `0.2154` n `311`
- 1h: commodity avg `-0.0171` n `7`; crypto_alt avg `0.2911` n `223`; crypto_major avg `0.1837` n `7`; equity avg `-0.083` n `42`; fx avg `0.0095` n `4`; index avg `0.0155` n `9`; metal avg `-0.0074` n `7`; unknown avg `0.0742` n `311`
- 4h: commodity avg `0.2238` n `7`; crypto_alt avg `-0.1684` n `223`; crypto_major avg `-0.1057` n `7`; equity avg `0.3151` n `42`; fx avg `0.0254` n `4`; index avg `0.0325` n `9`; metal avg `-0.126` n `7`; unknown avg `0.0371` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6858`, n `24`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6611`, n `24`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5589`, n `24`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5377`, n `24`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.5147`, n `24`, strong_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.5084`, n `24`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5069`, n `24`, strong_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3716`, n `24`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3521`, n `24`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2927`, n `24`, moderate_sample_signal
