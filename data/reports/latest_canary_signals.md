# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T01:07:29.791219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.0369` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `-0.1089` n `113`; fx avg `-0.0237` n `6`; index avg `-0.0265` n `25`; metal avg `0.0111` n `20`; unknown avg `0.0873` n `785`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `0.2061` n `230`; crypto_major avg `0.0781` n `8`; equity avg `0.2646` n `113`; fx avg `-0.0822` n `6`; index avg `0.0706` n `25`; metal avg `0.0546` n `20`; unknown avg `0.0749` n `785`
- 4h: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.158` n `230`; crypto_major avg `-0.4281` n `8`; equity avg `-0.0754` n `113`; fx avg `-0.0688` n `6`; index avg `-0.0098` n `25`; metal avg `0.0923` n `20`; unknown avg `-0.0838` n `785`
- 24h: commodity avg `0.7834` n `12`; crypto_alt avg `-0.4853` n `230`; crypto_major avg `-0.6247` n `8`; equity avg `-1.2916` n `113`; fx avg `0.1042` n `6`; index avg `-0.0439` n `25`; metal avg `0.6392` n `20`; unknown avg `103.7334` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
