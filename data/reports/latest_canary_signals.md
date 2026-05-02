# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T14:45:18.740045+00:00`
- Correlation status: `ready`
- Asset price records: `82`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `7`; crypto_alt avg `0.0306` n `223`; crypto_major avg `0.0136` n `7`; equity avg `0.0068` n `42`; fx avg `0.0005` n `4`; index avg `-0.0001` n `9`; metal avg `-0.0074` n `7`; unknown avg `-0.0029` n `313`
- 1h: commodity avg `0.0019` n `7`; crypto_alt avg `0.4128` n `223`; crypto_major avg `-0.0127` n `7`; equity avg `-0.0963` n `42`; fx avg `0.0123` n `4`; index avg `-0.0093` n `9`; metal avg `-0.0065` n `7`; unknown avg `0.1211` n `313`
- 4h: commodity avg `-0.0312` n `7`; crypto_alt avg `0.7281` n `223`; crypto_major avg `0.1991` n `7`; equity avg `-0.017` n `42`; fx avg `-0.0128` n `4`; index avg `0.0427` n `9`; metal avg `-0.016` n `7`; unknown avg `0.1297` n `313`
- 24h: commodity avg `0.3403` n `7`; crypto_alt avg `0.9456` n `223`; crypto_major avg `0.102` n `7`; equity avg `0.7157` n `42`; fx avg `-0.1415` n `4`; index avg `0.0376` n `9`; metal avg `-0.4087` n `7`; unknown avg `1.0106` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5381`, n `78`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5272`, n `74`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5207`, n `74`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5195`, n `78`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4781`, n `74`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4701`, n `74`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4655`, n `74`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4529`, n `78`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4374`, n `78`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4247`, n `74`, moderate_sample_signal
