# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T13:07:27.030279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1036` n `12`; crypto_alt avg `0.6038` n `228`; crypto_major avg `0.6966` n `8`; equity avg `-0.2873` n `74`; fx avg `0.0048` n `6`; index avg `-0.1154` n `23`; metal avg `-0.5106` n `18`; unknown avg `1.0968` n `424`
- 1h: commodity avg `-0.3157` n `12`; crypto_alt avg `0.1112` n `228`; crypto_major avg `0.2479` n `8`; equity avg `-0.4562` n `74`; fx avg `-0.0509` n `6`; index avg `-0.2916` n `23`; metal avg `-1.2364` n `18`; unknown avg `-0.2121` n `424`
- 4h: commodity avg `-0.446` n `12`; crypto_alt avg `0.1731` n `228`; crypto_major avg `0.2326` n `8`; equity avg `-0.5253` n `74`; fx avg `-0.006` n `6`; index avg `-0.2958` n `23`; metal avg `-0.7596` n `18`; unknown avg `2.3054` n `424`
- 24h: commodity avg `-0.4351` n `12`; crypto_alt avg `-5.7645` n `228`; crypto_major avg `-3.9055` n `8`; equity avg `-1.2624` n `74`; fx avg `0.0679` n `6`; index avg `-0.3661` n `23`; metal avg `-2.2178` n `18`; unknown avg `-0.3116` n `404`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
