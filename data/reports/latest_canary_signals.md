# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T03:37:27.700238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.0149` n `229`; crypto_major avg `-0.0202` n `8`; equity avg `-0.0956` n `91`; fx avg `0.0157` n `6`; index avg `-0.0462` n `25`; metal avg `-0.0248` n `20`; unknown avg `-0.0699` n `763`
- 1h: commodity avg `-0.0816` n `12`; crypto_alt avg `-0.2762` n `229`; crypto_major avg `-0.3011` n `8`; equity avg `-0.2817` n `91`; fx avg `-0.0572` n `6`; index avg `-0.0624` n `25`; metal avg `-0.2027` n `20`; unknown avg `1.4094` n `763`
- 4h: commodity avg `-0.0182` n `12`; crypto_alt avg `-1.2047` n `229`; crypto_major avg `-1.1977` n `8`; equity avg `-1.175` n `91`; fx avg `-0.1041` n `6`; index avg `-0.3712` n `25`; metal avg `-0.322` n `20`; unknown avg `0.7508` n `761`
- 24h: commodity avg `0.2884` n `12`; crypto_alt avg `-0.3018` n `229`; crypto_major avg `-0.8137` n `8`; equity avg `-1.3212` n `90`; fx avg `-0.0235` n `6`; index avg `-0.2569` n `25`; metal avg `-0.3371` n `20`; unknown avg `-0.3151` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
