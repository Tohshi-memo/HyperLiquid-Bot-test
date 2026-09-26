# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T13:22:27.935060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.4203` n `234`; crypto_major avg `-0.2822` n `8`; equity avg `-0.0107` n `141`; fx avg `-0.0058` n `6`; index avg `0.0044` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.0637` n `961`
- 1h: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.5032` n `234`; crypto_major avg `-0.2439` n `8`; equity avg `-0.01` n `141`; fx avg `0.0052` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.1548` n `959`
- 4h: commodity avg `0.0116` n `12`; crypto_alt avg `0.4537` n `234`; crypto_major avg `0.1249` n `8`; equity avg `0.0873` n `141`; fx avg `0.0227` n `6`; index avg `-0.0113` n `26`; metal avg `0.0008` n `20`; unknown avg `1.3797` n `949`
- 24h: commodity avg `0.196` n `12`; crypto_alt avg `1.5279` n `234`; crypto_major avg `-0.8328` n `8`; equity avg `-0.7523` n `141`; fx avg `0.0239` n `6`; index avg `0.0202` n `26`; metal avg `0.0714` n `20`; unknown avg `1121.0962` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
