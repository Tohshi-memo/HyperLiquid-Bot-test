# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T14:22:27.787263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `-0.047` n `239`; crypto_major avg `0.0056` n `8`; equity avg `-0.0197` n `158`; fx avg `-0.007` n `6`; index avg `0.0002` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.0896` n `1261`
- 1h: commodity avg `0.0362` n `13`; crypto_alt avg `0.0912` n `239`; crypto_major avg `0.1959` n `8`; equity avg `0.0034` n `158`; fx avg `-0.0363` n `6`; index avg `0.0159` n `27`; metal avg `0.0073` n `20`; unknown avg `0.1195` n `1255`
- 4h: commodity avg `0.0269` n `13`; crypto_alt avg `-0.1078` n `239`; crypto_major avg `-0.1126` n `8`; equity avg `0.058` n `158`; fx avg `0.0195` n `6`; index avg `0.0267` n `27`; metal avg `-0.0003` n `20`; unknown avg `-0.1104` n `1249`
- 24h: commodity avg `0.1034` n `13`; crypto_alt avg `-1.1603` n `239`; crypto_major avg `-0.1801` n `8`; equity avg `-0.5529` n `158`; fx avg `0.0097` n `6`; index avg `-0.0028` n `27`; metal avg `0.2372` n `20`; unknown avg `-0.0741` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
