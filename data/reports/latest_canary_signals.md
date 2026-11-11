# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T11:37:41.584867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `13`; crypto_alt avg `-0.1249` n `239`; crypto_major avg `-0.16` n `8`; equity avg `0.0473` n `161`; fx avg `-0.0061` n `6`; index avg `0.0022` n `27`; metal avg `-0.0401` n `20`; unknown avg `0.2357` n `1261`
- 1h: commodity avg `-0.0868` n `13`; crypto_alt avg `-0.2324` n `239`; crypto_major avg `-0.29` n `8`; equity avg `0.2332` n `161`; fx avg `-0.0037` n `6`; index avg `0.0458` n `27`; metal avg `-0.0264` n `20`; unknown avg `0.0719` n `1255`
- 4h: commodity avg `0.2931` n `13`; crypto_alt avg `0.4062` n `239`; crypto_major avg `0.3576` n `8`; equity avg `1.0285` n `161`; fx avg `-0.0439` n `6`; index avg `0.057` n `27`; metal avg `0.0487` n `20`; unknown avg `41.1446` n `1223`
- 24h: commodity avg `0.6682` n `13`; crypto_alt avg `-0.5749` n `239`; crypto_major avg `-1.2437` n `8`; equity avg `3.0765` n `161`; fx avg `-0.2227` n `6`; index avg `0.2922` n `27`; metal avg `0.2906` n `20`; unknown avg `2.1266` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
