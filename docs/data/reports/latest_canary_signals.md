# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T20:37:24.879585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `0.0431` n `8`; equity avg `-0.0136` n `113`; fx avg `-0.0069` n `6`; index avg `0.0022` n `25`; metal avg `0.0193` n `20`; unknown avg `1.0939` n `785`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0598` n `230`; crypto_major avg `0.0479` n `8`; equity avg `-0.3305` n `113`; fx avg `-0.0059` n `6`; index avg `-0.0367` n `25`; metal avg `-0.006` n `20`; unknown avg `3.7854` n `785`
- 4h: commodity avg `0.1496` n `12`; crypto_alt avg `0.0031` n `230`; crypto_major avg `0.4524` n `8`; equity avg `-0.3916` n `113`; fx avg `0.0196` n `6`; index avg `-0.0396` n `25`; metal avg `0.1897` n `20`; unknown avg `0.8094` n `785`
- 24h: commodity avg `1.2017` n `12`; crypto_alt avg `-0.98` n `230`; crypto_major avg `-0.895` n `8`; equity avg `-1.7273` n `113`; fx avg `0.2582` n `6`; index avg `-0.1021` n `25`; metal avg `0.167` n `20`; unknown avg `103.6216` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
