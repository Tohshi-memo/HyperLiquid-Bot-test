# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T10:37:25.854747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1707` n `228`; crypto_major avg `-0.2213` n `8`; equity avg `0.0289` n `74`; fx avg `0.0335` n `6`; index avg `0.0555` n `23`; metal avg `-0.005` n `18`; unknown avg `-0.0083` n `516`
- 1h: commodity avg `0.0387` n `12`; crypto_alt avg `-0.4839` n `228`; crypto_major avg `-0.5478` n `8`; equity avg `-0.3497` n `74`; fx avg `0.0303` n `6`; index avg `-0.2089` n `23`; metal avg `-0.142` n `18`; unknown avg `-3.2219` n `516`
- 4h: commodity avg `-0.2255` n `12`; crypto_alt avg `-0.21` n `228`; crypto_major avg `0.1688` n `8`; equity avg `-0.2976` n `74`; fx avg `0.0018` n `6`; index avg `-0.3041` n `23`; metal avg `-0.0002` n `18`; unknown avg `-4.8518` n `516`
- 24h: commodity avg `0.1474` n `12`; crypto_alt avg `4.1035` n `228`; crypto_major avg `3.8023` n `8`; equity avg `2.238` n `74`; fx avg `0.0556` n `6`; index avg `0.6857` n `23`; metal avg `0.6708` n `18`; unknown avg `0.4192` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
