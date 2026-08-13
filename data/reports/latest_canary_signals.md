# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T12:29:58.568934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0729` n `12`; crypto_alt avg `0.0755` n `230`; crypto_major avg `0.1263` n `8`; equity avg `0.0096` n `113`; fx avg `-0.0062` n `6`; index avg `0.0118` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0733` n `787`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `0.1141` n `8`; equity avg `0.0018` n `113`; fx avg `-0.0117` n `6`; index avg `0.0111` n `25`; metal avg `0.0282` n `20`; unknown avg `-0.0646` n `787`
- 4h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.0376` n `230`; crypto_major avg `-0.3312` n `8`; equity avg `0.13` n `113`; fx avg `-0.0111` n `6`; index avg `0.0336` n `25`; metal avg `0.2011` n `20`; unknown avg `-0.0289` n `787`
- 24h: commodity avg `-0.441` n `12`; crypto_alt avg `-0.8962` n `230`; crypto_major avg `-0.8258` n `8`; equity avg `1.0031` n `113`; fx avg `0.0083` n `6`; index avg `0.1436` n `25`; metal avg `-0.4122` n `20`; unknown avg `0.0829` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
