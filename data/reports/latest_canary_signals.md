# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T04:52:13.181650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `-0.0169` n `228`; crypto_major avg `-0.029` n `8`; equity avg `0.0361` n `65`; fx avg `0.0` n `5`; index avg `0.0237` n `23`; metal avg `0.0308` n `18`; unknown avg `-0.1121` n `376`
- 1h: commodity avg `-0.0503` n `12`; crypto_alt avg `0.028` n `228`; crypto_major avg `-0.0009` n `8`; equity avg `0.1212` n `65`; fx avg `0.0006` n `5`; index avg `0.0442` n `23`; metal avg `0.1134` n `18`; unknown avg `0.2471` n `376`
- 4h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.1484` n `228`; crypto_major avg `0.1994` n `8`; equity avg `0.3459` n `65`; fx avg `0.0032` n `5`; index avg `0.102` n `23`; metal avg `0.2259` n `18`; unknown avg `-0.0914` n `376`
- 24h: commodity avg `0.2257` n `12`; crypto_alt avg `-1.4758` n `228`; crypto_major avg `-0.6358` n `8`; equity avg `1.0441` n `65`; fx avg `-0.0062` n `5`; index avg `0.3212` n `23`; metal avg `0.3953` n `18`; unknown avg `-0.0777` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
