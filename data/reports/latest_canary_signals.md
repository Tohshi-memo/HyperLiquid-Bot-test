# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T20:37:40.579616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `0.2465` n `236`; crypto_major avg `0.1638` n `8`; equity avg `0.0816` n `151`; fx avg `0.0024` n `6`; index avg `0.0069` n `26`; metal avg `0.0091` n `20`; unknown avg `0.8616` n `1193`
- 1h: commodity avg `-0.023` n `13`; crypto_alt avg `0.4743` n `236`; crypto_major avg `0.4502` n `8`; equity avg `0.219` n `151`; fx avg `0.013` n `6`; index avg `0.014` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.4737` n `1115`
- 4h: commodity avg `0.0726` n `13`; crypto_alt avg `-0.7764` n `236`; crypto_major avg `-0.3578` n `8`; equity avg `-1.1725` n `151`; fx avg `0.0158` n `6`; index avg `-0.2428` n `26`; metal avg `-0.0274` n `20`; unknown avg `0.4573` n `1112`
- 24h: commodity avg `0.3286` n `13`; crypto_alt avg `-1.8906` n `236`; crypto_major avg `-1.7983` n `8`; equity avg `-3.9616` n `151`; fx avg `0.0192` n `6`; index avg `-0.6721` n `26`; metal avg `-0.1046` n `20`; unknown avg `0.3496` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1608`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
