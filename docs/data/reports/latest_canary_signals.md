# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T22:03:25.686472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `13`; crypto_alt avg `0.1051` n `239`; crypto_major avg `0.0918` n `8`; equity avg `0.0058` n `158`; fx avg `-0.0064` n `6`; index avg `0.0064` n `27`; metal avg `0.0025` n `20`; unknown avg `-0.3629` n `1252`
- 1h: commodity avg `-0.0075` n `13`; crypto_alt avg `0.2181` n `239`; crypto_major avg `0.2646` n `8`; equity avg `-0.0156` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0088` n `27`; metal avg `0.0018` n `20`; unknown avg `0.5698` n `1248`
- 4h: commodity avg `0.0746` n `13`; crypto_alt avg `-0.8337` n `239`; crypto_major avg `-0.3099` n `8`; equity avg `-0.1604` n `158`; fx avg `0.0038` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0064` n `20`; unknown avg `-0.1385` n `1212`
- 24h: commodity avg `0.0703` n `13`; crypto_alt avg `-2.0005` n `239`; crypto_major avg `-1.0004` n `8`; equity avg `-0.3162` n `158`; fx avg `-0.0101` n `6`; index avg `0.034` n `27`; metal avg `-0.0253` n `20`; unknown avg `146.6273` n `1095`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
