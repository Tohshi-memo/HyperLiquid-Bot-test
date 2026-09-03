# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T05:22:24.319891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.6024` n `232`; crypto_major avg `-0.6636` n `8`; equity avg `-0.5536` n `133`; fx avg `-0.016` n `6`; index avg `-0.1369` n `26`; metal avg `-0.0777` n `20`; unknown avg `5.5658` n `792`
- 1h: commodity avg `-0.1003` n `12`; crypto_alt avg `-0.2307` n `232`; crypto_major avg `-0.423` n `8`; equity avg `-0.8474` n `133`; fx avg `0.0248` n `6`; index avg `-0.2046` n `26`; metal avg `-0.1147` n `20`; unknown avg `2.7021` n `790`
- 4h: commodity avg `-0.1401` n `12`; crypto_alt avg `0.1102` n `232`; crypto_major avg `-0.0803` n `8`; equity avg `-0.5221` n `133`; fx avg `-0.0366` n `6`; index avg `-0.1587` n `26`; metal avg `0.082` n `20`; unknown avg `2.6073` n `790`
- 24h: commodity avg `0.0945` n `12`; crypto_alt avg `-0.2227` n `232`; crypto_major avg `-0.3647` n `8`; equity avg `0.7056` n `133`; fx avg `-0.3289` n `6`; index avg `-0.0064` n `26`; metal avg `0.7236` n `20`; unknown avg `-0.0307` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
