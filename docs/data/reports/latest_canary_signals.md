# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T08:22:30.623319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.1462` n `230`; crypto_major avg `-0.0154` n `8`; equity avg `0.1662` n `102`; fx avg `-0.0281` n `6`; index avg `0.0044` n `25`; metal avg `0.0079` n `20`; unknown avg `0.0006` n `780`
- 1h: commodity avg `-0.0867` n `12`; crypto_alt avg `0.3254` n `230`; crypto_major avg `0.0306` n `8`; equity avg `0.4232` n `102`; fx avg `-0.0617` n `6`; index avg `0.0189` n `25`; metal avg `0.006` n `20`; unknown avg `0.0038` n `779`
- 4h: commodity avg `-0.0231` n `12`; crypto_alt avg `0.2618` n `230`; crypto_major avg `-0.1295` n `8`; equity avg `0.2745` n `102`; fx avg `-0.1617` n `6`; index avg `0.0746` n `25`; metal avg `-0.0386` n `20`; unknown avg `-0.0429` n `747`
- 24h: commodity avg `-0.4815` n `12`; crypto_alt avg `0.1594` n `230`; crypto_major avg `0.4794` n `8`; equity avg `8.7367` n `102`; fx avg `-0.2272` n `6`; index avg `1.2636` n `25`; metal avg `0.4105` n `20`; unknown avg `0.0171` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
