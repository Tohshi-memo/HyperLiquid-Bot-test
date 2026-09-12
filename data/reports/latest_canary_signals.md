# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T15:37:32.867964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `0.0226` n `233`; crypto_major avg `-0.0931` n `8`; equity avg `-0.0081` n `136`; fx avg `-0.0007` n `6`; index avg `0.0049` n `26`; metal avg `-0.0018` n `20`; unknown avg `1.6354` n `838`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.1722` n `233`; crypto_major avg `-0.1244` n `8`; equity avg `-0.0015` n `136`; fx avg `0.0` n `6`; index avg `0.0074` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.4603` n `836`
- 4h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.3542` n `233`; crypto_major avg `-0.0231` n `8`; equity avg `-0.0298` n `136`; fx avg `0.0076` n `6`; index avg `0.0128` n `26`; metal avg `0.0322` n `20`; unknown avg `1.4327` n `824`
- 24h: commodity avg `-0.171` n `12`; crypto_alt avg `-0.8154` n `233`; crypto_major avg `-1.7754` n `8`; equity avg `-0.4616` n `136`; fx avg `-0.0096` n `6`; index avg `-0.0081` n `26`; metal avg `-0.1067` n `20`; unknown avg `10.6631` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
