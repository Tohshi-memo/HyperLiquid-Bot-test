# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T10:07:29.850483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.2009` n `233`; crypto_major avg `0.1239` n `8`; equity avg `0.0727` n `136`; fx avg `0.0128` n `6`; index avg `0.029` n `26`; metal avg `0.0318` n `20`; unknown avg `0.136` n `794`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.3447` n `233`; crypto_major avg `-0.2629` n `8`; equity avg `-0.094` n `136`; fx avg `0.0029` n `6`; index avg `0.0103` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.1502` n `794`
- 4h: commodity avg `-0.2849` n `12`; crypto_alt avg `-0.484` n `233`; crypto_major avg `-0.2051` n `8`; equity avg `0.353` n `136`; fx avg `-0.0745` n `6`; index avg `0.1001` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.2544` n `786`
- 24h: commodity avg `0.2908` n `12`; crypto_alt avg `-1.2571` n `233`; crypto_major avg `-1.4465` n `8`; equity avg `-0.8334` n `136`; fx avg `-0.0581` n `6`; index avg `-0.0932` n `26`; metal avg `-0.7778` n `20`; unknown avg `1.3172` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
