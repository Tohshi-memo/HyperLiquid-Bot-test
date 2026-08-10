# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T11:52:34.005677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `-0.009` n `230`; crypto_major avg `-0.0253` n `8`; equity avg `-0.0863` n `113`; fx avg `0.0001` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.0055` n `784`
- 1h: commodity avg `0.0459` n `12`; crypto_alt avg `0.0425` n `230`; crypto_major avg `0.032` n `8`; equity avg `-0.2515` n `113`; fx avg `0.0038` n `6`; index avg `-0.0461` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.054` n `784`
- 4h: commodity avg `0.3343` n `12`; crypto_alt avg `0.0428` n `230`; crypto_major avg `-0.1726` n `8`; equity avg `-0.4731` n `113`; fx avg `0.0146` n `6`; index avg `-0.0746` n `25`; metal avg `-0.1474` n `20`; unknown avg `-0.0545` n `784`
- 24h: commodity avg `0.6624` n `12`; crypto_alt avg `0.9023` n `230`; crypto_major avg `0.0859` n `8`; equity avg `-0.4141` n `113`; fx avg `0.2257` n `6`; index avg `0.01` n `25`; metal avg `-0.1608` n `20`; unknown avg `57.066` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
