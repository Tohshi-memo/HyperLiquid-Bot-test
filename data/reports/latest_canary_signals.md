# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T16:22:25.480918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `0.0576` n `239`; crypto_major avg `0.0249` n `8`; equity avg `-0.0102` n `158`; fx avg `0.0039` n `6`; index avg `-0.0065` n `27`; metal avg `0.0022` n `20`; unknown avg `-0.0218` n `1261`
- 1h: commodity avg `0.0241` n `13`; crypto_alt avg `-0.1328` n `239`; crypto_major avg `-0.1349` n `8`; equity avg `-0.0926` n `158`; fx avg `-0.0149` n `6`; index avg `0.0094` n `27`; metal avg `-0.0079` n `20`; unknown avg `0.3163` n `1241`
- 4h: commodity avg `0.0206` n `13`; crypto_alt avg `-0.3844` n `239`; crypto_major avg `-0.357` n `8`; equity avg `-0.1061` n `158`; fx avg `-0.0302` n `6`; index avg `0.0329` n `27`; metal avg `-0.01` n `20`; unknown avg `0.3636` n `1241`
- 24h: commodity avg `0.1537` n `13`; crypto_alt avg `-1.4691` n `239`; crypto_major avg `-0.4583` n `8`; equity avg `0.5667` n `158`; fx avg `-0.0134` n `6`; index avg `0.026` n `27`; metal avg `0.004` n `20`; unknown avg `-0.2475` n `1111`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
