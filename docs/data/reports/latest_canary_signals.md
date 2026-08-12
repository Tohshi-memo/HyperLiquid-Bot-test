# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T02:07:31.976803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0124` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `-0.03` n `113`; fx avg `0.0018` n `6`; index avg `-0.027` n `25`; metal avg `-0.0254` n `20`; unknown avg `0.0941` n `786`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.1308` n `230`; crypto_major avg `0.1064` n `8`; equity avg `0.2358` n `113`; fx avg `0.0393` n `6`; index avg `0.0436` n `25`; metal avg `0.0007` n `20`; unknown avg `0.0239` n `786`
- 4h: commodity avg `0.09` n `12`; crypto_alt avg `0.1952` n `230`; crypto_major avg `0.1752` n `8`; equity avg `0.5599` n `113`; fx avg `0.034` n `6`; index avg `0.0775` n `25`; metal avg `0.0686` n `20`; unknown avg `-0.1822` n `786`
- 24h: commodity avg `0.2122` n `12`; crypto_alt avg `-1.216` n `230`; crypto_major avg `0.8696` n `8`; equity avg `1.4749` n `113`; fx avg `-0.0018` n `6`; index avg `0.0881` n `25`; metal avg `-0.3003` n `20`; unknown avg `-0.1021` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.23`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2243`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
