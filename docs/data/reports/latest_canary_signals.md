# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T08:30:25.491349+00:00`
- Correlation status: `ready`
- Asset price records: `57`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `7`; crypto_alt avg `0.0146` n `223`; crypto_major avg `0.0482` n `7`; equity avg `-0.0074` n `42`; fx avg `-0.0008` n `4`; index avg `0.0023` n `9`; metal avg `0.0106` n `7`; unknown avg `-0.0116` n `313`
- 1h: commodity avg `0.0562` n `7`; crypto_alt avg `-0.0586` n `223`; crypto_major avg `0.1016` n `7`; equity avg `0.0246` n `42`; fx avg `0.0448` n `4`; index avg `0.0081` n `9`; metal avg `0.0262` n `7`; unknown avg `0.3588` n `311`
- 4h: commodity avg `0.0266` n `7`; crypto_alt avg `0.1067` n `223`; crypto_major avg `0.1796` n `7`; equity avg `0.2678` n `42`; fx avg `-0.0698` n `4`; index avg `-0.0134` n `9`; metal avg `0.0713` n `7`; unknown avg `0.2603` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5988`, n `53`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5857`, n `49`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5779`, n `53`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5445`, n `49`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4864`, n `53`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4647`, n `49`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.45`, n `53`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4476`, n `49`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4422`, n `53`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.437`, n `49`, moderate_sample_signal
