# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T14:52:25.903843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.6434` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `0.0065` n `230`; crypto_major avg `-0.0021` n `8`; equity avg `-0.6487` n `102`; fx avg `0.0578` n `6`; index avg `-0.0583` n `25`; metal avg `-0.0555` n `20`; unknown avg `-0.0183` n `779`
- 1h: commodity avg `0.2216` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `0.1214` n `8`; equity avg `0.4633` n `102`; fx avg `0.026` n `6`; index avg `0.0792` n `25`; metal avg `-0.0546` n `20`; unknown avg `0.1316` n `779`
- 4h: commodity avg `0.1959` n `12`; crypto_alt avg `0.5562` n `230`; crypto_major avg `0.5246` n `8`; equity avg `4.168` n `102`; fx avg `-0.2554` n `6`; index avg `0.4664` n `25`; metal avg `0.1186` n `20`; unknown avg `0.0504` n `779`
- 24h: commodity avg `-0.0739` n `12`; crypto_alt avg `0.9184` n `230`; crypto_major avg `1.0235` n `8`; equity avg `4.2138` n `102`; fx avg `-0.309` n `6`; index avg `0.5122` n `25`; metal avg `0.7863` n `20`; unknown avg `-0.0841` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
