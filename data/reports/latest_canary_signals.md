# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T08:00:26.480217+00:00`
- Correlation status: `ready`
- Asset price records: `55`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `7`; crypto_alt avg `-0.0205` n `223`; crypto_major avg `-0.0239` n `7`; equity avg `0.0094` n `42`; fx avg `-0.0104` n `4`; index avg `-0.0246` n `9`; metal avg `0.003` n `7`; unknown avg `0.0209` n `313`
- 1h: commodity avg `0.0098` n `7`; crypto_alt avg `0.0296` n `223`; crypto_major avg `-0.0931` n `7`; equity avg `-0.0065` n `42`; fx avg `0.0144` n `4`; index avg `-0.0419` n `9`; metal avg `0.0222` n `7`; unknown avg `0.1241` n `311`
- 4h: commodity avg `-0.0027` n `7`; crypto_alt avg `-0.1199` n `223`; crypto_major avg `-0.0895` n `7`; equity avg `0.1454` n `42`; fx avg `-0.1279` n `4`; index avg `-0.0579` n `9`; metal avg `0.0397` n `7`; unknown avg `0.0904` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6044`, n `51`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5849`, n `47`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5833`, n `51`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5457`, n `51`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5457`, n `47`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.511`, n `51`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4725`, n `51`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4653`, n `47`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4471`, n `47`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4401`, n `47`, moderate_sample_signal
