# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T20:37:28.589723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `0.1757` n `239`; crypto_major avg `0.0552` n `8`; equity avg `0.074` n `168`; fx avg `0.0064` n `6`; index avg `0.0277` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.2463` n `1265`
- 1h: commodity avg `0.0624` n `13`; crypto_alt avg `-0.0919` n `239`; crypto_major avg `-0.2785` n `8`; equity avg `0.0565` n `168`; fx avg `0.0014` n `6`; index avg `0.0138` n `27`; metal avg `0.1444` n `20`; unknown avg `5.3986` n `1255`
- 4h: commodity avg `0.0862` n `13`; crypto_alt avg `0.0406` n `239`; crypto_major avg `-0.558` n `8`; equity avg `0.4596` n `168`; fx avg `-0.0121` n `6`; index avg `0.0768` n `27`; metal avg `0.2465` n `20`; unknown avg `327.7787` n `1224`
- 24h: commodity avg `-0.5086` n `13`; crypto_alt avg `-0.0153` n `239`; crypto_major avg `-0.1834` n `8`; equity avg `3.2433` n `168`; fx avg `-0.1516` n `6`; index avg `0.3271` n `27`; metal avg `0.9388` n `20`; unknown avg `266.6494` n `1039`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
