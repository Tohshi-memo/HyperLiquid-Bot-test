# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T00:22:13.322962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2145` n `12`; crypto_alt avg `0.1766` n `228`; crypto_major avg `0.1417` n `8`; equity avg `0.1227` n `66`; fx avg `0.0046` n `6`; index avg `0.0445` n `23`; metal avg `-0.1032` n `18`; unknown avg `-0.0049` n `384`
- 1h: commodity avg `0.3725` n `12`; crypto_alt avg `0.4166` n `228`; crypto_major avg `0.5827` n `8`; equity avg `0.1051` n `66`; fx avg `0.0439` n `6`; index avg `0.0053` n `23`; metal avg `-0.0253` n `18`; unknown avg `2.4537` n `384`
- 4h: commodity avg `0.3909` n `12`; crypto_alt avg `0.4182` n `228`; crypto_major avg `1.0101` n `8`; equity avg `0.2698` n `66`; fx avg `0.0369` n `6`; index avg `-0.0937` n `23`; metal avg `-0.2012` n `18`; unknown avg `2.5056` n `384`
- 24h: commodity avg `-1.9525` n `12`; crypto_alt avg `3.4646` n `228`; crypto_major avg `3.3993` n `8`; equity avg `2.2302` n `66`; fx avg `-0.0649` n `6`; index avg `1.3416` n `23`; metal avg `1.352` n `18`; unknown avg `3.9969` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
