# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T15:35:04.104428+00:00`
- Correlation status: `ready`
- Asset price records: `85`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `7`; crypto_alt avg `0.0215` n `223`; crypto_major avg `0.0132` n `7`; equity avg `0.0041` n `42`; fx avg `0.0008` n `4`; index avg `-0.0046` n `9`; metal avg `0.0014` n `7`; unknown avg `0.0024` n `313`
- 1h: commodity avg `-0.0146` n `7`; crypto_alt avg `0.3278` n `223`; crypto_major avg `0.0825` n `7`; equity avg `0.0215` n `42`; fx avg `0.0357` n `4`; index avg `-0.0073` n `9`; metal avg `0.0072` n `7`; unknown avg `-0.1213` n `313`
- 4h: commodity avg `-0.0366` n `7`; crypto_alt avg `1.1468` n `223`; crypto_major avg `0.2566` n `7`; equity avg `-0.013` n `42`; fx avg `0.0368` n `4`; index avg `0.0221` n `9`; metal avg `-0.0034` n `7`; unknown avg `-0.0424` n `313`
- 24h: commodity avg `0.279` n `7`; crypto_alt avg `1.1505` n `223`; crypto_major avg `-0.1048` n `7`; equity avg `0.564` n `42`; fx avg `-0.112` n `4`; index avg `0.0659` n `9`; metal avg `-0.3288` n `7`; unknown avg `0.875` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5389`, n `77`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5339`, n `81`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5299`, n `77`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5153`, n `81`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4785`, n `77`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4777`, n `77`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4655`, n `77`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4522`, n `81`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4318`, n `81`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4257`, n `77`, moderate_sample_signal
