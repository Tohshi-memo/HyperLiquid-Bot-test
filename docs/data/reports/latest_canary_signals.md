# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T19:37:31.330127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `-0.1288` n `236`; crypto_major avg `-0.1071` n `8`; equity avg `-0.0806` n `151`; fx avg `-0.0052` n `6`; index avg `-0.018` n `26`; metal avg `-0.0426` n `20`; unknown avg `7.3703` n `1136`
- 1h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.1599` n `236`; crypto_major avg `0.3015` n `8`; equity avg `0.0588` n `151`; fx avg `0.0147` n `6`; index avg `0.0038` n `26`; metal avg `-0.0106` n `20`; unknown avg `7.4889` n `1134`
- 4h: commodity avg `0.0747` n `13`; crypto_alt avg `0.0873` n `236`; crypto_major avg `-0.2367` n `8`; equity avg `-0.8565` n `151`; fx avg `0.0244` n `6`; index avg `-0.14` n `26`; metal avg `-0.0716` n `20`; unknown avg `6.8197` n `1124`
- 24h: commodity avg `-0.1785` n `13`; crypto_alt avg `-2.5475` n `236`; crypto_major avg `-2.0482` n `8`; equity avg `-3.8847` n `151`; fx avg `-0.1567` n `6`; index avg `-0.5425` n `26`; metal avg `-0.8736` n `20`; unknown avg `1272.3862` n `976`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.062`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0619`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0585`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0555`, n `666`, weak_sample_signal
