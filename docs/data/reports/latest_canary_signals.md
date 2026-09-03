# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T04:52:26.737622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.3272` n `232`; crypto_major avg `0.2872` n `8`; equity avg `-0.0153` n `133`; fx avg `0.0226` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.9614` n `792`
- 1h: commodity avg `-0.049` n `12`; crypto_alt avg `0.4567` n `232`; crypto_major avg `0.1045` n `8`; equity avg `-0.0184` n `133`; fx avg `0.0051` n `6`; index avg `-0.0128` n `26`; metal avg `0.0421` n `20`; unknown avg `1.3973` n `790`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `1.2038` n `232`; crypto_major avg `1.0021` n `8`; equity avg `0.3099` n `133`; fx avg `-0.0803` n `6`; index avg `0.0564` n `26`; metal avg `0.2427` n `20`; unknown avg `204.6667` n `790`
- 24h: commodity avg `0.1702` n `12`; crypto_alt avg `0.519` n `232`; crypto_major avg `0.4198` n `8`; equity avg `1.6232` n `133`; fx avg `-0.3614` n `6`; index avg `0.2084` n `26`; metal avg `0.9377` n `20`; unknown avg `2.1661` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
