# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T20:37:21.150540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.0779` n `228`; crypto_major avg `-0.0298` n `8`; equity avg `0.0552` n `65`; fx avg `0.0161` n `5`; index avg `-0.0164` n `23`; metal avg `0.0032` n `18`; unknown avg `0.0332` n `376`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.1035` n `228`; crypto_major avg `-0.0742` n `8`; equity avg `0.2356` n `65`; fx avg `0.0283` n `5`; index avg `-0.0134` n `23`; metal avg `0.0693` n `18`; unknown avg `0.0876` n `376`
- 4h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.4862` n `228`; crypto_major avg `0.2187` n `8`; equity avg `0.3487` n `65`; fx avg `0.0172` n `5`; index avg `0.01` n `23`; metal avg `0.1433` n `18`; unknown avg `0.2102` n `376`
- 24h: commodity avg `0.4003` n `12`; crypto_alt avg `0.4742` n `228`; crypto_major avg `0.367` n `8`; equity avg `0.7997` n `65`; fx avg `-0.022` n `5`; index avg `0.3244` n `23`; metal avg `0.042` n `18`; unknown avg `0.1451` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
