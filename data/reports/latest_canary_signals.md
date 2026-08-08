# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T21:37:29.724118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.0059` n `230`; crypto_major avg `0.0062` n `8`; equity avg `0.0081` n `112`; fx avg `-0.0006` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.0639` n `784`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0561` n `230`; crypto_major avg `0.0291` n `8`; equity avg `0.0052` n `112`; fx avg `0.0022` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.1483` n `784`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.0054` n `230`; crypto_major avg `-0.1787` n `8`; equity avg `0.0945` n `112`; fx avg `0.0013` n `6`; index avg `0.0041` n `25`; metal avg `0.005` n `20`; unknown avg `0.3048` n `784`
- 24h: commodity avg `0.1194` n `12`; crypto_alt avg `1.7914` n `230`; crypto_major avg `1.4065` n `8`; equity avg `0.6712` n `112`; fx avg `0.0014` n `6`; index avg `0.0261` n `25`; metal avg `0.0479` n `20`; unknown avg `0.198` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0443`, n `668`, weak_sample_signal
