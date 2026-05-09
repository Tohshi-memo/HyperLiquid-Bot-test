# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T23:52:12.851860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `0.0066` n `228`; crypto_major avg `0.005` n `8`; equity avg `0.0168` n `65`; fx avg `0.0102` n `5`; index avg `0.0071` n `23`; metal avg `-0.0013` n `18`; unknown avg `-0.1775` n `376`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.3674` n `228`; crypto_major avg `-0.1971` n `8`; equity avg `0.0461` n `65`; fx avg `0.0093` n `5`; index avg `0.0403` n `23`; metal avg `-0.0233` n `18`; unknown avg `0.1886` n `376`
- 4h: commodity avg `-0.0565` n `12`; crypto_alt avg `-0.3821` n `228`; crypto_major avg `-0.2987` n `8`; equity avg `0.4529` n `65`; fx avg `0.0093` n `5`; index avg `0.146` n `23`; metal avg `0.0982` n `18`; unknown avg `0.0277` n `376`
- 24h: commodity avg `0.417` n `12`; crypto_alt avg `-0.1252` n `228`; crypto_major avg `0.2435` n `8`; equity avg `0.8076` n `65`; fx avg `-0.0134` n `5`; index avg `0.3387` n `23`; metal avg `0.3646` n `18`; unknown avg `0.3889` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
