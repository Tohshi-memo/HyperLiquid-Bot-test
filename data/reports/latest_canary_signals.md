# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T00:07:28.275597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `13`; crypto_alt avg `0.0813` n `239`; crypto_major avg `0.0483` n `8`; equity avg `0.2129` n `166`; fx avg `-0.0173` n `6`; index avg `0.0986` n `27`; metal avg `0.0824` n `20`; unknown avg `-0.0874` n `1252`
- 1h: commodity avg `0.0759` n `13`; crypto_alt avg `0.3414` n `239`; crypto_major avg `-0.2275` n `8`; equity avg `-0.352` n `166`; fx avg `-0.0342` n `6`; index avg `-0.0461` n `27`; metal avg `-0.0614` n `20`; unknown avg `-0.2308` n `1250`
- 4h: commodity avg `0.1832` n `13`; crypto_alt avg `-0.5439` n `239`; crypto_major avg `-0.6517` n `8`; equity avg `0.5992` n `166`; fx avg `-0.0206` n `6`; index avg `0.0656` n `27`; metal avg `-0.0051` n `20`; unknown avg `98.7492` n `1216`
- 24h: commodity avg `-1.0293` n `13`; crypto_alt avg `0.8423` n `239`; crypto_major avg `0.6483` n `8`; equity avg `5.2705` n `166`; fx avg `-0.1884` n `6`; index avg `0.4484` n `27`; metal avg `0.3096` n `20`; unknown avg `327.4373` n `1051`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
