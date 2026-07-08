# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T22:22:32.694354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.1402` n `229`; crypto_major avg `-0.1447` n `8`; equity avg `0.0276` n `91`; fx avg `0.0087` n `6`; index avg `-0.0006` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0931` n `764`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `0.4914` n `229`; crypto_major avg `0.346` n `8`; equity avg `0.2174` n `91`; fx avg `0.034` n `6`; index avg `0.0158` n `25`; metal avg `0.0289` n `20`; unknown avg `0.084` n `764`
- 4h: commodity avg `0.2388` n `12`; crypto_alt avg `0.0341` n `229`; crypto_major avg `-0.058` n `8`; equity avg `0.5873` n `91`; fx avg `0.0228` n `6`; index avg `0.0153` n `25`; metal avg `0.0044` n `20`; unknown avg `0.9919` n `764`
- 24h: commodity avg `0.3964` n `12`; crypto_alt avg `-1.458` n `229`; crypto_major avg `-2.2303` n `8`; equity avg `1.4052` n `91`; fx avg `0.0392` n `6`; index avg `-0.0108` n `25`; metal avg `-0.7254` n `20`; unknown avg `0.0697` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
