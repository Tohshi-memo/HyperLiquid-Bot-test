# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T20:30:29.584701+00:00`
- Correlation status: `ready`
- Asset price records: `105`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `7`; crypto_alt avg `0.0266` n `223`; crypto_major avg `0.0155` n `7`; equity avg `-0.0` n `42`; fx avg `0.0088` n `4`; index avg `0.0` n `9`; metal avg `0.0056` n `7`; unknown avg `0.1592` n `313`
- 1h: commodity avg `-0.0429` n `7`; crypto_alt avg `0.052` n `223`; crypto_major avg `-0.1044` n `7`; equity avg `0.056` n `42`; fx avg `0.0109` n `4`; index avg `-0.0004` n `9`; metal avg `-0.0028` n `7`; unknown avg `0.1792` n `313`
- 4h: commodity avg `-0.2125` n `7`; crypto_alt avg `0.4474` n `223`; crypto_major avg `-0.0161` n `7`; equity avg `0.3192` n `42`; fx avg `0.05` n `4`; index avg `0.0457` n `9`; metal avg `-0.0405` n `7`; unknown avg `0.2763` n `313`
- 24h: commodity avg `-0.0584` n `7`; crypto_alt avg `1.6383` n `223`; crypto_major avg `0.2055` n `7`; equity avg `0.949` n `42`; fx avg `-0.0114` n `4`; index avg `0.0612` n `9`; metal avg `-0.097` n `7`; unknown avg `0.3433` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5255`, n `97`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5074`, n `101`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5055`, n `97`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4898`, n `101`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4461`, n `97`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4307`, n `97`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4269`, n `97`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.419`, n `101`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.418`, n `97`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4168`, n `97`, moderate_sample_signal
