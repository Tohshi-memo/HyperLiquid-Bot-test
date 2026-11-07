# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T21:52:23.273304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `0.2049` n `239`; crypto_major avg `0.1554` n `8`; equity avg `0.0181` n `158`; fx avg `0.0069` n `6`; index avg `-0.0008` n `27`; metal avg `0.0019` n `20`; unknown avg `2.3389` n `1262`
- 1h: commodity avg `0.0194` n `13`; crypto_alt avg `0.0592` n `239`; crypto_major avg `0.1945` n `8`; equity avg `-0.06` n `158`; fx avg `0.0048` n `6`; index avg `-0.0075` n `27`; metal avg `-0.0032` n `20`; unknown avg `1.4812` n `1236`
- 4h: commodity avg `0.0632` n `13`; crypto_alt avg `-0.8675` n `239`; crypto_major avg `-0.3508` n `8`; equity avg `-0.1738` n `158`; fx avg `0.0114` n `6`; index avg `-0.0264` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.4265` n `1206`
- 24h: commodity avg `0.1012` n `13`; crypto_alt avg `-2.0341` n `239`; crypto_major avg `-0.8202` n `8`; equity avg `-0.2897` n `158`; fx avg `-0.0087` n `6`; index avg `0.0412` n `27`; metal avg `-0.012` n `20`; unknown avg `146.8187` n `1095`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
