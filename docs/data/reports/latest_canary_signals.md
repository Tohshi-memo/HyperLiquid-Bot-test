# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T12:37:36.106594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `-0.2306` n `8`; equity avg `-0.0982` n `113`; fx avg `-0.0005` n `6`; index avg `-0.0181` n `25`; metal avg `0.0219` n `20`; unknown avg `0.0119` n `784`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `-0.0556` n `230`; crypto_major avg `-0.0817` n `8`; equity avg `-0.4249` n `113`; fx avg `-0.0124` n `6`; index avg `-0.0613` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0105` n `784`
- 4h: commodity avg `0.2578` n `12`; crypto_alt avg `-0.0734` n `230`; crypto_major avg `-0.1704` n `8`; equity avg `-0.7917` n `113`; fx avg `-0.0097` n `6`; index avg `-0.115` n `25`; metal avg `-0.0634` n `20`; unknown avg `-0.048` n `784`
- 24h: commodity avg `0.8527` n `10`; crypto_alt avg `0.8606` n `228`; crypto_major avg `0.1302` n `7`; equity avg `-0.7774` n `109`; fx avg `0.1983` n `6`; index avg `-0.0298` n `24`; metal avg `-0.2311` n `13`; unknown avg `58.2754` n `736`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
