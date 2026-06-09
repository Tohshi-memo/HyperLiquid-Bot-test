# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T14:22:26.435897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1804` n `12`; crypto_alt avg `-0.8835` n `228`; crypto_major avg `-0.5938` n `8`; equity avg `-0.5627` n `74`; fx avg `0.0014` n `6`; index avg `-0.3797` n `23`; metal avg `-0.2559` n `18`; unknown avg `0.2435` n `545`
- 1h: commodity avg `-0.2281` n `12`; crypto_alt avg `-1.1211` n `228`; crypto_major avg `-1.0609` n `8`; equity avg `-1.3028` n `74`; fx avg `-0.0205` n `6`; index avg `-0.6917` n `23`; metal avg `-0.6571` n `18`; unknown avg `-0.1185` n `545`
- 4h: commodity avg `-0.4566` n `12`; crypto_alt avg `-0.6335` n `228`; crypto_major avg `-1.4447` n `8`; equity avg `-1.27` n `74`; fx avg `0.0471` n `6`; index avg `-0.7453` n `23`; metal avg `-0.5142` n `18`; unknown avg `-0.374` n `545`
- 24h: commodity avg `-0.7521` n `12`; crypto_alt avg `-2.2957` n `228`; crypto_major avg `-2.6179` n `8`; equity avg `0.0275` n `74`; fx avg `0.1197` n `6`; index avg `-0.0539` n `23`; metal avg `0.3086` n `18`; unknown avg `-1.316` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
