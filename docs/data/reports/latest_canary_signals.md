# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T15:22:12.781474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.0641` n `228`; crypto_major avg `0.0662` n `8`; equity avg `0.0347` n `65`; fx avg `-0.0013` n `5`; index avg `-0.0042` n `23`; metal avg `-0.0189` n `18`; unknown avg `0.0934` n `376`
- 1h: commodity avg `0.213` n `12`; crypto_alt avg `-0.3433` n `228`; crypto_major avg `-0.3357` n `8`; equity avg `0.0923` n `65`; fx avg `0.0119` n `5`; index avg `-0.0228` n `23`; metal avg `-0.0718` n `18`; unknown avg `0.1605` n `376`
- 4h: commodity avg `0.4006` n `12`; crypto_alt avg `-1.0432` n `228`; crypto_major avg `-0.6441` n `8`; equity avg `0.0325` n `65`; fx avg `0.0032` n `5`; index avg `0.021` n `23`; metal avg `-0.0875` n `18`; unknown avg `0.0446` n `376`
- 24h: commodity avg `-0.2465` n `12`; crypto_alt avg `1.6902` n `228`; crypto_major avg `1.4452` n `8`; equity avg `1.6597` n `65`; fx avg `0.0321` n `5`; index avg `0.7125` n `23`; metal avg `0.1296` n `18`; unknown avg `0.3201` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
