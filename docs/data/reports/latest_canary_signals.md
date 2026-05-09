# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T20:30:57.984314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `-0.0504` n `228`; crypto_major avg `-0.0209` n `8`; equity avg `0.0509` n `65`; fx avg `0.017` n `5`; index avg `0.0108` n `23`; metal avg `-0.006` n `18`; unknown avg `0.0473` n `376`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.076` n `228`; crypto_major avg `-0.0654` n `8`; equity avg `0.2309` n `65`; fx avg `0.0291` n `5`; index avg `0.0137` n `23`; metal avg `0.0602` n `18`; unknown avg `0.0997` n `376`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.5136` n `228`; crypto_major avg `0.2276` n `8`; equity avg `0.3439` n `65`; fx avg `0.0181` n `5`; index avg `0.0372` n `23`; metal avg `0.1341` n `18`; unknown avg `0.2157` n `376`
- 24h: commodity avg `0.402` n `12`; crypto_alt avg `0.5014` n `228`; crypto_major avg `0.376` n `8`; equity avg `0.7963` n `65`; fx avg `-0.0212` n `5`; index avg `0.3519` n `23`; metal avg `0.033` n `18`; unknown avg `0.1403` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
