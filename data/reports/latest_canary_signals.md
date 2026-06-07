# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T12:00:48.880696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0759` n `228`; crypto_major avg `0.0195` n `8`; equity avg `-0.0224` n `74`; fx avg `0.0` n `6`; index avg `-0.0644` n `23`; metal avg `-0.0342` n `18`; unknown avg `-0.0072` n `516`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `0.4324` n `228`; crypto_major avg `0.325` n `8`; equity avg `0.2508` n `74`; fx avg `0.0003` n `6`; index avg `0.0456` n `23`; metal avg `-0.0147` n `18`; unknown avg `-0.0217` n `516`
- 4h: commodity avg `0.1028` n `12`; crypto_alt avg `0.3166` n `228`; crypto_major avg `0.2879` n `8`; equity avg `0.0284` n `74`; fx avg `-0.0342` n `6`; index avg `-0.1305` n `23`; metal avg `-0.0405` n `18`; unknown avg `-4.7079` n `516`
- 24h: commodity avg `0.0764` n `12`; crypto_alt avg `2.869` n `228`; crypto_major avg `2.6579` n `8`; equity avg `1.8834` n `74`; fx avg `0.0208` n `6`; index avg `0.579` n `23`; metal avg `0.507` n `18`; unknown avg `0.1145` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
