# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T13:37:26.834365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `13`; crypto_alt avg `0.2363` n `239`; crypto_major avg `0.139` n `8`; equity avg `0.0678` n `158`; fx avg `0.0002` n `6`; index avg `0.0143` n `27`; metal avg `0.0065` n `20`; unknown avg `0.0083` n `1261`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `0.2559` n `239`; crypto_major avg `0.0672` n `8`; equity avg `0.1361` n `158`; fx avg `0.008` n `6`; index avg `0.0198` n `27`; metal avg `0.001` n `20`; unknown avg `0.5206` n `1255`
- 4h: commodity avg `0.0542` n `13`; crypto_alt avg `-0.1891` n `239`; crypto_major avg `-0.2211` n `8`; equity avg `0.005` n `158`; fx avg `0.0578` n `6`; index avg `0.0014` n `27`; metal avg `0.012` n `20`; unknown avg `-0.1314` n `1249`
- 24h: commodity avg `-0.1076` n `13`; crypto_alt avg `-1.185` n `239`; crypto_major avg `-0.38` n `8`; equity avg `-0.126` n `158`; fx avg `0.0454` n `6`; index avg `0.0021` n `27`; metal avg `0.1424` n `20`; unknown avg `0.0994` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
