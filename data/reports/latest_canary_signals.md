# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T19:22:25.982967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.1765` n `239`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0345` n `158`; fx avg `0.005` n `6`; index avg `-0.012` n `27`; metal avg `-0.0137` n `20`; unknown avg `0.3203` n `1262`
- 1h: commodity avg `0.0161` n `13`; crypto_alt avg `-0.3437` n `239`; crypto_major avg `-0.1434` n `8`; equity avg `-0.1144` n `158`; fx avg `0.0004` n `6`; index avg `-0.0119` n `27`; metal avg `-0.0126` n `20`; unknown avg `-0.0664` n `1256`
- 4h: commodity avg `0.0343` n `13`; crypto_alt avg `-0.0588` n `239`; crypto_major avg `-0.0264` n `8`; equity avg `0.0268` n `158`; fx avg `-0.0196` n `6`; index avg `0.0182` n `27`; metal avg `-0.0233` n `20`; unknown avg `0.3515` n `1209`
- 24h: commodity avg `-0.0393` n `13`; crypto_alt avg `-1.4164` n `239`; crypto_major avg `-0.4508` n `8`; equity avg `0.3365` n `158`; fx avg `-0.0116` n `6`; index avg `0.0488` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.1453` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
