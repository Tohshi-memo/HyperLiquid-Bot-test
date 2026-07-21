# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T07:52:31.381182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0332` n `12`; crypto_alt avg `0.0189` n `230`; crypto_major avg `0.0339` n `8`; equity avg `-0.0095` n `98`; fx avg `-0.002` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0475` n `20`; unknown avg `-0.026` n `771`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0471` n `230`; crypto_major avg `0.0377` n `8`; equity avg `0.0334` n `98`; fx avg `0.0057` n `6`; index avg `-0.0154` n `25`; metal avg `0.0151` n `20`; unknown avg `-0.0485` n `771`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `0.4963` n `230`; crypto_major avg `0.5589` n `8`; equity avg `0.3996` n `98`; fx avg `0.0442` n `6`; index avg `0.0126` n `25`; metal avg `0.386` n `20`; unknown avg `0.0457` n `755`
- 24h: commodity avg `-0.0069` n `12`; crypto_alt avg `2.6171` n `230`; crypto_major avg `2.7332` n `8`; equity avg `1.6487` n `98`; fx avg `-0.106` n `6`; index avg `0.2908` n `25`; metal avg `0.6143` n `20`; unknown avg `0.1786` n `753`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0759`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
