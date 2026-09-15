# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T06:52:30.649473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.2036` n `233`; crypto_major avg `-0.2636` n `8`; equity avg `-0.0301` n `136`; fx avg `0.0107` n `6`; index avg `-0.0028` n `27`; metal avg `0.0159` n `20`; unknown avg `0.7558` n `908`
- 1h: commodity avg `0.1107` n `12`; crypto_alt avg `-0.417` n `233`; crypto_major avg `-0.4764` n `8`; equity avg `-0.2134` n `136`; fx avg `0.0257` n `6`; index avg `-0.0442` n `27`; metal avg `-0.0874` n `20`; unknown avg `0.5756` n `884`
- 4h: commodity avg `0.0689` n `12`; crypto_alt avg `-0.9043` n `233`; crypto_major avg `-1.0142` n `8`; equity avg `-0.7501` n `136`; fx avg `0.0413` n `6`; index avg `-0.1396` n `27`; metal avg `-0.1287` n `20`; unknown avg `3.411` n `868`
- 24h: commodity avg `0.0487` n `12`; crypto_alt avg `-1.4927` n `233`; crypto_major avg `-0.6664` n `8`; equity avg `-0.4965` n `136`; fx avg `0.15` n `6`; index avg `-0.0797` n `27`; metal avg `-0.3037` n `20`; unknown avg `4.7487` n `796`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
