# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:54:51.020025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.3043` n `230`; crypto_major avg `0.3466` n `8`; equity avg `0.0311` n `121`; fx avg `0.0029` n `6`; index avg `0.0023` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.2527` n `794`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `0.3197` n `230`; crypto_major avg `0.348` n `8`; equity avg `0.0508` n `121`; fx avg `-0.0038` n `6`; index avg `-0.0041` n `25`; metal avg `0.0026` n `20`; unknown avg `0.2976` n `794`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.3084` n `230`; crypto_major avg `0.2167` n `8`; equity avg `-0.0183` n `121`; fx avg `0.0002` n `6`; index avg `-0.0016` n `25`; metal avg `0.0147` n `20`; unknown avg `0.4326` n `794`
- 24h: commodity avg `-0.131` n `12`; crypto_alt avg `1.1375` n `230`; crypto_major avg `3.4534` n `8`; equity avg `-0.4837` n `121`; fx avg `0.0442` n `6`; index avg `-0.0546` n `25`; metal avg `-0.0983` n `20`; unknown avg `2.1442` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
