# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T10:37:30.017521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.063` n `12`; crypto_alt avg `-0.0693` n `230`; crypto_major avg `-0.0485` n `8`; equity avg `0.0602` n `92`; fx avg `0.0156` n `6`; index avg `0.0162` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.0139` n `766`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `0.1548` n `8`; equity avg `0.1231` n `92`; fx avg `0.0055` n `6`; index avg `0.0376` n `25`; metal avg `-0.0338` n `20`; unknown avg `-0.0097` n `766`
- 4h: commodity avg `0.108` n `12`; crypto_alt avg `-0.3105` n `230`; crypto_major avg `-0.0782` n `8`; equity avg `0.2404` n `92`; fx avg `0.0545` n `6`; index avg `0.0476` n `25`; metal avg `-0.0973` n `20`; unknown avg `-0.1691` n `766`
- 24h: commodity avg `1.3469` n `12`; crypto_alt avg `-1.0162` n `230`; crypto_major avg `-0.5053` n `8`; equity avg `-0.34` n `92`; fx avg `-0.005` n `6`; index avg `-0.042` n `25`; metal avg `-0.1` n `20`; unknown avg `-0.3192` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
