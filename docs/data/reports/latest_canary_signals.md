# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T19:55:59.530346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0345` n `230`; crypto_major avg `0.0123` n `8`; equity avg `0.0111` n `92`; fx avg `0.0016` n `6`; index avg `0.0023` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0589` n `765`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `0.0411` n `230`; crypto_major avg `-0.0144` n `8`; equity avg `0.0259` n `92`; fx avg `-0.0006` n `6`; index avg `0.0132` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.1673` n `765`
- 4h: commodity avg `0.0221` n `12`; crypto_alt avg `0.3872` n `230`; crypto_major avg `0.2697` n `8`; equity avg `0.2616` n `92`; fx avg `0.0073` n `6`; index avg `0.0111` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0627` n `765`
- 24h: commodity avg `-0.0192` n `12`; crypto_alt avg `1.085` n `229`; crypto_major avg `0.6932` n `8`; equity avg `0.344` n `92`; fx avg `-0.0012` n `6`; index avg `0.0407` n `25`; metal avg `0.0502` n `20`; unknown avg `2.3464` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
