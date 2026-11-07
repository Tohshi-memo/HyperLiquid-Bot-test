# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T06:22:30.270583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `-0.1324` n `239`; crypto_major avg `-0.013` n `8`; equity avg `0.0064` n `158`; fx avg `-0.0168` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0039` n `20`; unknown avg `-0.0618` n `1261`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `-0.1262` n `239`; crypto_major avg `0.1576` n `8`; equity avg `-0.0759` n `158`; fx avg `-0.0182` n `6`; index avg `0.0003` n `27`; metal avg `-0.0074` n `20`; unknown avg `0.2023` n `1229`
- 4h: commodity avg `-0.0705` n `13`; crypto_alt avg `-0.4006` n `239`; crypto_major avg `-0.2988` n `8`; equity avg `-0.1068` n `158`; fx avg `-0.0237` n `6`; index avg `0.0068` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.0222` n `1207`
- 24h: commodity avg `-0.3074` n `13`; crypto_alt avg `0.3823` n `239`; crypto_major avg `0.4149` n `8`; equity avg `1.4486` n `158`; fx avg `-0.06` n `6`; index avg `0.2183` n `27`; metal avg `0.2343` n `20`; unknown avg `8.4149` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
