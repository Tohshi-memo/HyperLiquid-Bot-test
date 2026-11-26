# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T04:07:25.340483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.0471` n `239`; crypto_major avg `0.0438` n `8`; equity avg `0.2366` n `168`; fx avg `-0.0142` n `6`; index avg `0.0149` n `27`; metal avg `-0.0029` n `20`; unknown avg `1.906` n `1249`
- 1h: commodity avg `0.0837` n `13`; crypto_alt avg `-0.0487` n `239`; crypto_major avg `0.1903` n `8`; equity avg `0.3101` n `168`; fx avg `-0.0232` n `6`; index avg `0.0203` n `27`; metal avg `-0.0182` n `20`; unknown avg `4.0222` n `1253`
- 4h: commodity avg `0.1195` n `13`; crypto_alt avg `0.773` n `239`; crypto_major avg `0.8406` n `8`; equity avg `0.9628` n `168`; fx avg `-0.0527` n `6`; index avg `0.0858` n `27`; metal avg `0.1736` n `20`; unknown avg `163.8103` n `1245`
- 24h: commodity avg `0.7831` n `13`; crypto_alt avg `3.8721` n `239`; crypto_major avg `3.2078` n `8`; equity avg `2.5338` n `168`; fx avg `0.0012` n `6`; index avg `0.1881` n `27`; metal avg `0.623` n `20`; unknown avg `774.1662` n `1013`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
