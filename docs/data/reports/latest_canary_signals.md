# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T08:52:29.391400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `13`; crypto_alt avg `-0.0553` n `239`; crypto_major avg `-0.0348` n `8`; equity avg `-0.0008` n `158`; fx avg `0.0079` n `6`; index avg `0.0008` n `27`; metal avg `0.0002` n `20`; unknown avg `0.0116` n `1247`
- 1h: commodity avg `0.0031` n `13`; crypto_alt avg `-0.2116` n `239`; crypto_major avg `0.0485` n `8`; equity avg `0.1098` n `158`; fx avg `-0.0127` n `6`; index avg `0.0128` n `27`; metal avg `0.0058` n `20`; unknown avg `0.0105` n `1215`
- 4h: commodity avg `0.0544` n `13`; crypto_alt avg `-0.0934` n `239`; crypto_major avg `0.4098` n `8`; equity avg `-0.0284` n `158`; fx avg `-0.0311` n `6`; index avg `0.0164` n `27`; metal avg `-0.0074` n `20`; unknown avg `0.2364` n `1187`
- 24h: commodity avg `-0.001` n `13`; crypto_alt avg `-0.047` n `239`; crypto_major avg `0.4501` n `8`; equity avg `0.7617` n `158`; fx avg `-0.0007` n `6`; index avg `0.1127` n `27`; metal avg `-0.0228` n `20`; unknown avg `8.1006` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
