# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T16:37:39.551290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `0.1013` n `230`; crypto_major avg `0.1108` n `8`; equity avg `-0.0967` n `113`; fx avg `0.0045` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0483` n `20`; unknown avg `0.0696` n `785`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.0007` n `230`; crypto_major avg `-0.0674` n `8`; equity avg `-0.0348` n `113`; fx avg `0.0016` n `6`; index avg `0.01` n `25`; metal avg `0.0836` n `20`; unknown avg `-0.0538` n `785`
- 4h: commodity avg `0.3799` n `12`; crypto_alt avg `-0.5985` n `230`; crypto_major avg `-0.9298` n `8`; equity avg `-0.3656` n `113`; fx avg `0.0471` n `6`; index avg `0.0117` n `25`; metal avg `0.2063` n `20`; unknown avg `1.5131` n `784`
- 24h: commodity avg `1.166` n `12`; crypto_alt avg `-0.6951` n `230`; crypto_major avg `-1.4891` n `8`; equity avg `-1.2484` n `113`; fx avg `0.2437` n `6`; index avg `-0.043` n `25`; metal avg `0.0048` n `20`; unknown avg `103.3874` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
