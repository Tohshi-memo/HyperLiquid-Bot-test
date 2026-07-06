# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T15:07:39.722097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0552` n `12`; crypto_alt avg `0.3118` n `229`; crypto_major avg `0.4535` n `8`; equity avg `0.0301` n `88`; fx avg `0.0101` n `6`; index avg `-0.0037` n `25`; metal avg `0.1418` n `20`; unknown avg `0.2726` n `765`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.5697` n `229`; crypto_major avg `0.6283` n `8`; equity avg `0.1752` n `88`; fx avg `0.0089` n `6`; index avg `0.0321` n `25`; metal avg `0.0927` n `20`; unknown avg `0.2968` n `765`
- 4h: commodity avg `0.1004` n `12`; crypto_alt avg `-0.1129` n `229`; crypto_major avg `-0.7031` n `8`; equity avg `0.6601` n `88`; fx avg `0.0434` n `6`; index avg `0.1127` n `25`; metal avg `-0.1122` n `20`; unknown avg `-0.2831` n `765`
- 24h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.5553` n `229`; crypto_major avg `-1.0036` n `8`; equity avg `-0.1937` n `88`; fx avg `0.1911` n `6`; index avg `0.0468` n `25`; metal avg `-0.304` n `20`; unknown avg `0.4032` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
