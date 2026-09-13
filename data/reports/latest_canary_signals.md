# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T12:21:08.517061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.248` n `233`; crypto_major avg `0.057` n `8`; equity avg `-0.0041` n `136`; fx avg `0.0007` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0013` n `20`; unknown avg `1.3216` n `838`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.2197` n `233`; crypto_major avg `0.1419` n `8`; equity avg `-0.0784` n `136`; fx avg `-0.0066` n `6`; index avg `-0.0214` n `27`; metal avg `-0.0069` n `20`; unknown avg `1.5772` n `832`
- 4h: commodity avg `0.162` n `12`; crypto_alt avg `-0.3152` n `233`; crypto_major avg `-0.6811` n `8`; equity avg `-0.6979` n `136`; fx avg `0.0084` n `6`; index avg `-0.1313` n `27`; metal avg `-0.0488` n `20`; unknown avg `0.4226` n `826`
- 24h: commodity avg `0.2606` n `12`; crypto_alt avg `-0.5413` n `233`; crypto_major avg `-1.8523` n `8`; equity avg `-1.8384` n `136`; fx avg `0.0021` n `6`; index avg `-0.2991` n `26`; metal avg `-0.0809` n `20`; unknown avg `-0.35` n `704`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
