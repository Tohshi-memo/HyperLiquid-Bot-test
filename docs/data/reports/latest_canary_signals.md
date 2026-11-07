# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T12:37:24.140405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.1498` n `239`; crypto_major avg `-0.1475` n `8`; equity avg `-0.012` n `158`; fx avg `0.0072` n `6`; index avg `0.0018` n `27`; metal avg `0.0055` n `20`; unknown avg `0.1039` n `1261`
- 1h: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.0656` n `239`; crypto_major avg `-0.2146` n `8`; equity avg `-0.0464` n `158`; fx avg `0.045` n `6`; index avg `-0.0039` n `27`; metal avg `0.0052` n `20`; unknown avg `0.0859` n `1249`
- 4h: commodity avg `0.057` n `13`; crypto_alt avg `-0.68` n `239`; crypto_major avg `-0.5473` n `8`; equity avg `-0.0818` n `158`; fx avg `0.0616` n `6`; index avg `-0.016` n `27`; metal avg `-0.004` n `20`; unknown avg `133.9115` n `1219`
- 24h: commodity avg `0.0144` n `13`; crypto_alt avg `-1.5163` n `239`; crypto_major avg `-0.8435` n `8`; equity avg `-0.8022` n `158`; fx avg `-0.0039` n `6`; index avg `-0.0273` n `27`; metal avg `0.0136` n `20`; unknown avg `-0.5012` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
