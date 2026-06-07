# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T12:37:26.305882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3288` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1654` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.0832` n `228`; crypto_major avg `0.0204` n `8`; equity avg `-0.0461` n `74`; fx avg `0.0083` n `6`; index avg `-0.0448` n `23`; metal avg `-0.0794` n `18`; unknown avg `-0.0324` n `516`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `-1.5028` n `228`; crypto_major avg `-1.2899` n `8`; equity avg `-0.2274` n `74`; fx avg `0.0129` n `6`; index avg `0.0389` n `23`; metal avg `-0.1901` n `18`; unknown avg `-0.3118` n `516`
- 4h: commodity avg `0.2242` n `12`; crypto_alt avg `-1.4065` n `228`; crypto_major avg `-1.4464` n `8`; equity avg `-0.2553` n `74`; fx avg `-0.023` n `6`; index avg `-0.281` n `23`; metal avg `-0.2428` n `18`; unknown avg `-4.0291` n `516`
- 24h: commodity avg `0.1651` n `12`; crypto_alt avg `1.8048` n `228`; crypto_major avg `1.8664` n `8`; equity avg `1.4608` n `74`; fx avg `0.0276` n `6`; index avg `0.3789` n `23`; metal avg `0.3907` n `18`; unknown avg `-0.2986` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
