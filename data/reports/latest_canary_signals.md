# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T21:32:39.770671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0674` n `12`; crypto_alt avg `-0.1059` n `230`; crypto_major avg `-0.1081` n `8`; equity avg `-0.009` n `96`; fx avg `0.0007` n `6`; index avg `-0.0006` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0594` n `770`
- 1h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.0688` n `230`; crypto_major avg `0.0635` n `8`; equity avg `0.0108` n `96`; fx avg `0.0022` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.2052` n `770`
- 4h: commodity avg `0.08` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `0.317` n `8`; equity avg `-0.0146` n `96`; fx avg `-0.0077` n `6`; index avg `-0.0264` n `25`; metal avg `-0.0232` n `20`; unknown avg `0.2579` n `770`
- 24h: commodity avg `0.255` n `12`; crypto_alt avg `-0.2804` n `230`; crypto_major avg `0.3783` n `8`; equity avg `-0.2582` n `96`; fx avg `-0.0724` n `6`; index avg `0.0274` n `25`; metal avg `0.0028` n `20`; unknown avg `0.1127` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
