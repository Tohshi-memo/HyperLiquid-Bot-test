# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T19:37:27.543650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `13`; crypto_alt avg `-0.0242` n `239`; crypto_major avg `0.2029` n `8`; equity avg `0.0417` n `166`; fx avg `-0.0014` n `6`; index avg `0.0414` n `27`; metal avg `0.008` n `20`; unknown avg `1.2787` n `1262`
- 1h: commodity avg `0.0279` n `13`; crypto_alt avg `-0.3652` n `239`; crypto_major avg `0.2214` n `8`; equity avg `0.0702` n `166`; fx avg `-0.0074` n `6`; index avg `0.0512` n `27`; metal avg `0.0286` n `20`; unknown avg `40.8061` n `1246`
- 4h: commodity avg `0.0919` n `13`; crypto_alt avg `-0.3798` n `239`; crypto_major avg `0.6666` n `8`; equity avg `0.2288` n `166`; fx avg `0.005` n `6`; index avg `0.0631` n `27`; metal avg `0.0692` n `20`; unknown avg `166.7772` n `1198`
- 24h: commodity avg `0.2603` n `13`; crypto_alt avg `1.1192` n `239`; crypto_major avg `3.1407` n `8`; equity avg `1.1439` n `166`; fx avg `-0.091` n `6`; index avg `0.188` n `27`; metal avg `0.3149` n `20`; unknown avg `92.4526` n `1088`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
