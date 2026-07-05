# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T20:07:26.014896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.0911` n `229`; crypto_major avg `0.095` n `8`; equity avg `0.0099` n `88`; fx avg `-0.0129` n `6`; index avg `0.0029` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0208` n `765`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.0534` n `229`; crypto_major avg `0.1067` n `8`; equity avg `0.0269` n `88`; fx avg `-0.0051` n `6`; index avg `-0.003` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.0138` n `765`
- 4h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.5189` n `229`; crypto_major avg `0.1662` n `8`; equity avg `0.1265` n `88`; fx avg `-0.0026` n `6`; index avg `0.0137` n `25`; metal avg `0.0048` n `20`; unknown avg `0.746` n `763`
- 24h: commodity avg `-0.0201` n `12`; crypto_alt avg `-1.0897` n `229`; crypto_major avg `-0.5277` n `8`; equity avg `0.3302` n `88`; fx avg `-0.0411` n `6`; index avg `0.0906` n `25`; metal avg `0.0419` n `20`; unknown avg `1.0754` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
