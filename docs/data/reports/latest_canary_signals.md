# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T08:23:07.268011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `12`; crypto_alt avg `-0.2073` n `230`; crypto_major avg `-0.2449` n `8`; equity avg `-0.3345` n `102`; fx avg `0.0174` n `6`; index avg `-0.0374` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.0841` n `784`
- 1h: commodity avg `0.1141` n `12`; crypto_alt avg `-0.2466` n `230`; crypto_major avg `-0.2937` n `8`; equity avg `-0.647` n `102`; fx avg `0.0006` n `6`; index avg `-0.066` n `25`; metal avg `0.0439` n `20`; unknown avg `-0.1094` n `784`
- 4h: commodity avg `0.1222` n `12`; crypto_alt avg `-0.5509` n `230`; crypto_major avg `-0.756` n `8`; equity avg `-1.0268` n `102`; fx avg `-0.0019` n `6`; index avg `-0.1321` n `25`; metal avg `-0.0682` n `20`; unknown avg `-0.0357` n `768`
- 24h: commodity avg `-0.0442` n `12`; crypto_alt avg `-1.3774` n `230`; crypto_major avg `-1.1225` n `8`; equity avg `-0.3253` n `102`; fx avg `-0.1772` n `6`; index avg `-0.135` n `25`; metal avg `-0.1111` n `20`; unknown avg `0.9634` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
