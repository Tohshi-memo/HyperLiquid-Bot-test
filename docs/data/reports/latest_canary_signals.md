# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T17:52:26.135348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1551` n `233`; crypto_major avg `0.0698` n `8`; equity avg `0.0431` n `136`; fx avg `-0.0042` n `6`; index avg `-0.0028` n `27`; metal avg `-0.003` n `20`; unknown avg `2.6793` n `840`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.4376` n `233`; crypto_major avg `0.2134` n `8`; equity avg `0.1096` n `136`; fx avg `0.0003` n `6`; index avg `-0.0195` n `27`; metal avg `0.006` n `20`; unknown avg `0.9219` n `780`
- 4h: commodity avg `0.0019` n `12`; crypto_alt avg `0.3637` n `233`; crypto_major avg `0.7167` n `8`; equity avg `0.327` n `136`; fx avg `0.0053` n `6`; index avg `-0.0013` n `27`; metal avg `0.0262` n `20`; unknown avg `3.8343` n `774`
- 24h: commodity avg `0.2687` n `12`; crypto_alt avg `0.0441` n `233`; crypto_major avg `-0.8365` n `8`; equity avg `-1.3958` n `136`; fx avg `0.0102` n `6`; index avg `-0.2736` n `26`; metal avg `-0.0652` n `20`; unknown avg `1.6915` n `688`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
