# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T21:45:21.400606+00:00`
- Correlation status: `ready`
- Asset price records: `110`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `7`; crypto_alt avg `0.1745` n `223`; crypto_major avg `0.3398` n `7`; equity avg `-0.0008` n `42`; fx avg `-0.0069` n `4`; index avg `0.0074` n `9`; metal avg `0.008` n `7`; unknown avg `0.0167` n `313`
- 1h: commodity avg `0.0203` n `7`; crypto_alt avg `0.4494` n `223`; crypto_major avg `0.3566` n `7`; equity avg `0.1285` n `42`; fx avg `0.0239` n `4`; index avg `-0.0065` n `9`; metal avg `0.0049` n `7`; unknown avg `0.0806` n `313`
- 4h: commodity avg `-0.0524` n `7`; crypto_alt avg `0.7442` n `223`; crypto_major avg `0.4093` n `7`; equity avg `0.4637` n `42`; fx avg `0.0351` n `4`; index avg `0.0412` n `9`; metal avg `-0.0238` n `7`; unknown avg `0.2449` n `313`
- 24h: commodity avg `-0.0149` n `7`; crypto_alt avg `1.9917` n `223`; crypto_major avg `0.577` n `7`; equity avg `1.1336` n `42`; fx avg `0.0085` n `4`; index avg `0.0623` n `9`; metal avg `-0.0942` n `7`; unknown avg `0.3996` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5439`, n `102`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5404`, n `102`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4959`, n `106`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4787`, n `106`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4722`, n `102`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4203`, n `102`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4195`, n `102`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.418`, n `102`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4166`, n `102`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4118`, n `106`, moderate_sample_signal
