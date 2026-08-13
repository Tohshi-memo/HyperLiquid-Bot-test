# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T02:22:38.575412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0492` n `230`; crypto_major avg `0.0217` n `8`; equity avg `0.0268` n `113`; fx avg `-0.0006` n `6`; index avg `0.0054` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.074` n `786`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `-0.0203` n `230`; crypto_major avg `0.0154` n `8`; equity avg `0.2997` n `113`; fx avg `0.0165` n `6`; index avg `0.0317` n `25`; metal avg `-0.0636` n `20`; unknown avg `-0.2636` n `786`
- 4h: commodity avg `-0.1332` n `12`; crypto_alt avg `0.4822` n `230`; crypto_major avg `0.1461` n `8`; equity avg `0.6477` n `113`; fx avg `-0.0313` n `6`; index avg `0.0704` n `25`; metal avg `0.0431` n `20`; unknown avg `-0.2578` n `786`
- 24h: commodity avg `-0.2403` n `12`; crypto_alt avg `-1.4476` n `230`; crypto_major avg `-0.515` n `8`; equity avg `2.827` n `113`; fx avg `-0.0554` n `6`; index avg `0.3667` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.0243` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
