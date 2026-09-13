# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T22:07:24.211538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4388` n `12`; crypto_alt avg `-0.8306` n `233`; crypto_major avg `-0.555` n `8`; equity avg `-0.2849` n `136`; fx avg `-0.0038` n `6`; index avg `-0.1027` n `27`; metal avg `-0.0805` n `20`; unknown avg `4.909` n `838`
- 1h: commodity avg `0.2563` n `12`; crypto_alt avg `-1.0081` n `233`; crypto_major avg `-0.6821` n `8`; equity avg `-0.2` n `136`; fx avg `-0.0012` n `6`; index avg `-0.0763` n `27`; metal avg `-0.0716` n `20`; unknown avg `4.5501` n `838`
- 4h: commodity avg `0.3824` n `12`; crypto_alt avg `-1.0483` n `233`; crypto_major avg `-0.4743` n `8`; equity avg `-0.1825` n `136`; fx avg `0.0387` n `6`; index avg `-0.0699` n `27`; metal avg `-0.0715` n `20`; unknown avg `7.4685` n `794`
- 24h: commodity avg `0.6178` n `12`; crypto_alt avg `-0.7251` n `233`; crypto_major avg `-1.037` n `8`; equity avg `-1.303` n `136`; fx avg `0.0464` n `6`; index avg `-0.3091` n `26`; metal avg `-0.1192` n `20`; unknown avg `2.7411` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
