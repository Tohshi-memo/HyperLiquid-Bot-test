# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T21:22:29.441699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.3752` n `230`; crypto_major avg `-0.1462` n `8`; equity avg `-0.1184` n `113`; fx avg `0.0024` n `6`; index avg `-0.0` n `25`; metal avg `0.0034` n `20`; unknown avg `0.4219` n `785`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `-0.4465` n `230`; crypto_major avg `-0.1468` n `8`; equity avg `-0.1241` n `113`; fx avg `-0.012` n `6`; index avg `0.0127` n `25`; metal avg `0.0452` n `20`; unknown avg `0.4768` n `785`
- 4h: commodity avg `0.1114` n `12`; crypto_alt avg `-0.5106` n `230`; crypto_major avg `0.2045` n `8`; equity avg `-0.4483` n `113`; fx avg `0.0183` n `6`; index avg `-0.0389` n `25`; metal avg `0.2127` n `20`; unknown avg `1.3288` n `785`
- 24h: commodity avg `1.0733` n `12`; crypto_alt avg `-1.4011` n `230`; crypto_major avg `-1.0415` n `8`; equity avg `-1.8375` n `113`; fx avg `0.2682` n `6`; index avg `-0.0882` n `25`; metal avg `0.2374` n `20`; unknown avg `104.2191` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
