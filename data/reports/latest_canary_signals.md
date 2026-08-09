# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T03:37:31.494284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.1097` n `230`; crypto_major avg `0.0359` n `8`; equity avg `-0.005` n `112`; fx avg `-0.0012` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0301` n `784`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0503` n `112`; fx avg `0.007` n `6`; index avg `-0.0023` n `25`; metal avg `0.012` n `20`; unknown avg `-0.1268` n `784`
- 4h: commodity avg `0.0633` n `12`; crypto_alt avg `0.084` n `230`; crypto_major avg `-0.2302` n `8`; equity avg `-0.0665` n `112`; fx avg `0.0144` n `6`; index avg `-0.012` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.1757` n `784`
- 24h: commodity avg `0.2223` n `12`; crypto_alt avg `1.4211` n `230`; crypto_major avg `0.4726` n `8`; equity avg `0.5014` n `112`; fx avg `0.0001` n `6`; index avg `0.0284` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.0107` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
