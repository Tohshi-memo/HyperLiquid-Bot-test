# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T05:37:29.134747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.08` n `234`; crypto_major avg `0.1563` n `8`; equity avg `0.0504` n `140`; fx avg `-0.0026` n `6`; index avg `0.016` n `26`; metal avg `-0.0301` n `20`; unknown avg `0.9674` n `944`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `-0.011` n `234`; crypto_major avg `0.298` n `8`; equity avg `-0.0302` n `140`; fx avg `-0.0081` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0563` n `20`; unknown avg `53.3666` n `942`
- 4h: commodity avg `0.1019` n `12`; crypto_alt avg `0.6805` n `234`; crypto_major avg `-0.0318` n `8`; equity avg `-0.2319` n `140`; fx avg `-0.0211` n `6`; index avg `0.0214` n `26`; metal avg `-0.1435` n `20`; unknown avg `61.0756` n `936`
- 24h: commodity avg `-0.5187` n `12`; crypto_alt avg `3.5293` n `234`; crypto_major avg `2.7917` n `8`; equity avg `1.0594` n `140`; fx avg `-0.0014` n `6`; index avg `0.2211` n `26`; metal avg `-0.0073` n `20`; unknown avg `9.9753` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
