# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T18:15:17.757949+00:00`
- Correlation status: `ready`
- Asset price records: `96`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `7`; crypto_alt avg `-0.1824` n `223`; crypto_major avg `-0.0981` n `7`; equity avg `0.0008` n `42`; fx avg `0.0032` n `4`; index avg `0.0141` n `9`; metal avg `-0.001` n `7`; unknown avg `-0.0421` n `313`
- 1h: commodity avg `-0.1014` n `7`; crypto_alt avg `-0.3862` n `223`; crypto_major avg `-0.1835` n `7`; equity avg `0.1732` n `42`; fx avg `0.0` n `4`; index avg `0.0168` n `9`; metal avg `-0.0395` n `7`; unknown avg `-0.0667` n `313`
- 4h: commodity avg `-0.181` n `7`; crypto_alt avg `0.4512` n `223`; crypto_major avg `0.025` n `7`; equity avg `0.1477` n `42`; fx avg `0.0861` n `4`; index avg `0.0222` n `9`; metal avg `-0.0305` n `7`; unknown avg `0.1432` n `313`
- 24h: commodity avg `0.2122` n `7`; crypto_alt avg `1.1926` n `223`; crypto_major avg `0.191` n `7`; equity avg `0.7692` n `42`; fx avg `-0.0436` n `4`; index avg `0.1515` n `9`; metal avg `-0.4962` n `7`; unknown avg `0.7951` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5291`, n `88`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5239`, n `92`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5056`, n `92`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5042`, n `88`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.467`, n `88`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.446`, n `88`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.436`, n `92`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4348`, n `88`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4215`, n `88`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4176`, n `88`, moderate_sample_signal
