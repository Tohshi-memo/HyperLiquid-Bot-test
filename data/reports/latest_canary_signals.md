# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T19:15:19.814084+00:00`
- Correlation status: `ready`
- Asset price records: `100`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `7`; crypto_alt avg `0.0953` n `223`; crypto_major avg `0.0599` n `7`; equity avg `0.0879` n `42`; fx avg `0.0` n `4`; index avg `0.0071` n `9`; metal avg `-0.0145` n `7`; unknown avg `-0.0024` n `313`
- 1h: commodity avg `-0.0095` n `7`; crypto_alt avg `0.5345` n `223`; crypto_major avg `0.3198` n `7`; equity avg `0.0849` n `42`; fx avg `-0.0021` n `4`; index avg `0.0198` n `9`; metal avg `-0.0146` n `7`; unknown avg `0.122` n `313`
- 4h: commodity avg `-0.1711` n `7`; crypto_alt avg `0.5566` n `223`; crypto_major avg `0.1997` n `7`; equity avg `0.2652` n `42`; fx avg `0.0452` n `4`; index avg `0.0504` n `9`; metal avg `-0.0466` n `7`; unknown avg `0.1316` n `313`
- 24h: commodity avg `0.0189` n `7`; crypto_alt avg `1.4369` n `223`; crypto_major avg `0.3016` n `7`; equity avg `0.7954` n `42`; fx avg `-0.0308` n `4`; index avg `0.0993` n `9`; metal avg `-0.2902` n `7`; unknown avg `0.4414` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.525`, n `92`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5105`, n `96`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4957`, n `92`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4927`, n `96`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4496`, n `92`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4313`, n `92`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4249`, n `96`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.424`, n `92`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4209`, n `92`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4203`, n `92`, moderate_sample_signal
