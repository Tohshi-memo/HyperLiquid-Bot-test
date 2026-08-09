# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T04:52:27.570811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0521` n `230`; crypto_major avg `-0.0307` n `8`; equity avg `0.0198` n `112`; fx avg `0.0031` n `6`; index avg `0.0016` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.013` n `784`
- 1h: commodity avg `0.0526` n `12`; crypto_alt avg `0.2431` n `230`; crypto_major avg `0.0413` n `8`; equity avg `-0.0012` n `112`; fx avg `0.0039` n `6`; index avg `0.0025` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0341` n `784`
- 4h: commodity avg `0.1433` n `12`; crypto_alt avg `0.3285` n `230`; crypto_major avg `-0.1998` n `8`; equity avg `-0.0841` n `112`; fx avg `0.0124` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.2559` n `784`
- 24h: commodity avg `0.2661` n `12`; crypto_alt avg `1.7177` n `230`; crypto_major avg `0.48` n `8`; equity avg `0.5366` n `112`; fx avg `0.002` n `6`; index avg `0.0584` n `25`; metal avg `0.0248` n `20`; unknown avg `0.004` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
