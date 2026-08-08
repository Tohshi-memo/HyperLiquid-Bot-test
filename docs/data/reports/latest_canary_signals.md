# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T18:16:33.978667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0018` n `230`; crypto_major avg `-0.0356` n `8`; equity avg `0.0278` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.0041` n `784`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.0436` n `230`; crypto_major avg `-0.1045` n `8`; equity avg `0.071` n `112`; fx avg `-0.005` n `6`; index avg `0.0052` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0251` n `784`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `0.657` n `230`; crypto_major avg `0.3278` n `8`; equity avg `0.1956` n `112`; fx avg `-0.0064` n `6`; index avg `0.0119` n `25`; metal avg `0.0134` n `20`; unknown avg `0.121` n `784`
- 24h: commodity avg `-0.1965` n `12`; crypto_alt avg `1.5493` n `230`; crypto_major avg `1.4845` n `8`; equity avg `0.959` n `112`; fx avg `0.0037` n `6`; index avg `0.0948` n `25`; metal avg `0.1326` n `20`; unknown avg `0.1314` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
