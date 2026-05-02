# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T14:00:25.685194+00:00`
- Correlation status: `ready`
- Asset price records: `79`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `7`; crypto_alt avg `0.0693` n `223`; crypto_major avg `0.0088` n `7`; equity avg `0.0031` n `42`; fx avg `-0.0024` n `4`; index avg `-0.0025` n `9`; metal avg `0.0043` n `7`; unknown avg `0.06` n `313`
- 1h: commodity avg `0.0012` n `7`; crypto_alt avg `0.3531` n `223`; crypto_major avg `0.2596` n `7`; equity avg `0.0685` n `42`; fx avg `-0.0189` n `4`; index avg `-0.0006` n `9`; metal avg `-0.0303` n `7`; unknown avg `0.0922` n `313`
- 4h: commodity avg `-0.0403` n `7`; crypto_alt avg `0.3712` n `223`; crypto_major avg `0.1188` n `7`; equity avg `0.1346` n `42`; fx avg `-0.0213` n `4`; index avg `0.0534` n `9`; metal avg `-0.0089` n `7`; unknown avg `-0.0312` n `313`
- 24h: commodity avg `0.5345` n `7`; crypto_alt avg `0.2307` n `223`; crypto_major avg `-0.402` n `7`; equity avg `0.7838` n `42`; fx avg `-0.1276` n `4`; index avg `0.0575` n `9`; metal avg `-0.742` n `7`; unknown avg `0.9706` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5387`, n `75`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5201`, n `75`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5151`, n `71`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5083`, n `71`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4837`, n `75`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.474`, n `71`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4628`, n `71`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4627`, n `71`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4516`, n `75`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4418`, n `75`, moderate_sample_signal
