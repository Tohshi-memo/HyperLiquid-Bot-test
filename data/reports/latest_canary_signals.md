# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T07:52:20.440962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1349` n `12`; crypto_alt avg `0.0197` n `228`; crypto_major avg `-0.0375` n `8`; equity avg `-0.0627` n `74`; fx avg `-0.0125` n `6`; index avg `-0.0186` n `23`; metal avg `0.0036` n `18`; unknown avg `0.0168` n `516`
- 1h: commodity avg `-0.2217` n `12`; crypto_alt avg `-0.1557` n `228`; crypto_major avg `0.0251` n `8`; equity avg `-0.043` n `74`; fx avg `-0.0047` n `6`; index avg `-0.0608` n `23`; metal avg `-0.024` n `18`; unknown avg `-0.1384` n `516`
- 4h: commodity avg `-0.2939` n `12`; crypto_alt avg `1.0315` n `228`; crypto_major avg `1.5324` n `8`; equity avg `0.615` n `74`; fx avg `-0.0057` n `6`; index avg `-0.035` n `23`; metal avg `0.1809` n `18`; unknown avg `-0.0554` n `506`
- 24h: commodity avg `0.25` n `12`; crypto_alt avg `2.6407` n `228`; crypto_major avg `2.0017` n `8`; equity avg `2.49` n `74`; fx avg `0.0471` n `6`; index avg `1.1135` n `23`; metal avg `0.62` n `18`; unknown avg `0.6691` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
