# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T18:04:21.846097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1043` n `12`; crypto_alt avg `-0.0697` n `230`; crypto_major avg `-0.1495` n `8`; equity avg `0.162` n `92`; fx avg `-0.0032` n `6`; index avg `0.0065` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0623` n `766`
- 1h: commodity avg `0.3954` n `12`; crypto_alt avg `-0.6311` n `230`; crypto_major avg `-0.5161` n `8`; equity avg `-0.3242` n `92`; fx avg `-0.0243` n `6`; index avg `-0.0692` n `25`; metal avg `-0.0775` n `20`; unknown avg `-0.1668` n `766`
- 4h: commodity avg `0.9582` n `12`; crypto_alt avg `-0.9845` n `230`; crypto_major avg `-0.772` n `8`; equity avg `-0.4452` n `92`; fx avg `-0.035` n `6`; index avg `-0.1416` n `25`; metal avg `-0.2835` n `20`; unknown avg `-0.1952` n `766`
- 24h: commodity avg `0.5779` n `12`; crypto_alt avg `-2.3557` n `230`; crypto_major avg `-3.2336` n `8`; equity avg `-3.1387` n `92`; fx avg `-0.0788` n `6`; index avg `-0.6144` n `25`; metal avg `-0.6181` n `20`; unknown avg `-0.2363` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
