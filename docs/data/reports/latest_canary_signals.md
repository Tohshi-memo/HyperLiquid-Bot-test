# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T11:07:24.460623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0652` n `12`; crypto_alt avg `0.4283` n `231`; crypto_major avg `0.4097` n `8`; equity avg `0.0331` n `127`; fx avg `0.0022` n `6`; index avg `0.008` n `26`; metal avg `0.0275` n `20`; unknown avg `0.0222` n `792`
- 1h: commodity avg `0.0032` n `12`; crypto_alt avg `1.1713` n `231`; crypto_major avg `1.1061` n `8`; equity avg `0.1853` n `127`; fx avg `0.0664` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0454` n `20`; unknown avg `0.2561` n `792`
- 4h: commodity avg `-0.0731` n `12`; crypto_alt avg `0.3405` n `231`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0205` n `127`; fx avg `0.0471` n `6`; index avg `-0.0177` n `26`; metal avg `0.1387` n `20`; unknown avg `0.137` n `792`
- 24h: commodity avg `0.1707` n `12`; crypto_alt avg `-0.1805` n `231`; crypto_major avg `0.0992` n `8`; equity avg `-1.0347` n `127`; fx avg `-0.0249` n `6`; index avg `-0.0391` n `26`; metal avg `0.6947` n `20`; unknown avg `0.3822` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
