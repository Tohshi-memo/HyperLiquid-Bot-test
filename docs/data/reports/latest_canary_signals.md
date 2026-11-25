# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T11:07:30.708063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0993` n `13`; crypto_alt avg `0.1132` n `239`; crypto_major avg `0.1473` n `8`; equity avg `0.2931` n `168`; fx avg `-0.0116` n `6`; index avg `0.0162` n `27`; metal avg `0.0231` n `20`; unknown avg `30.9868` n `1229`
- 1h: commodity avg `-0.0957` n `13`; crypto_alt avg `-0.0614` n `239`; crypto_major avg `0.0034` n `8`; equity avg `0.1362` n `168`; fx avg `0.0031` n `6`; index avg `-0.025` n `27`; metal avg `-0.0899` n `20`; unknown avg `33.1265` n `1229`
- 4h: commodity avg `0.2343` n `13`; crypto_alt avg `-0.8958` n `239`; crypto_major avg `-1.1333` n `8`; equity avg `-1.069` n `168`; fx avg `0.0072` n `6`; index avg `-0.1533` n `27`; metal avg `-0.0435` n `20`; unknown avg `0.7954` n `1209`
- 24h: commodity avg `0.3467` n `13`; crypto_alt avg `-1.8714` n `239`; crypto_major avg `-2.454` n `8`; equity avg `-4.2087` n `167`; fx avg `0.0168` n `6`; index avg `-0.3755` n `27`; metal avg `-0.891` n `20`; unknown avg `488.4753` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
