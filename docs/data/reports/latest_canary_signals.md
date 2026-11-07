# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T17:22:28.665539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.1348` n `239`; crypto_major avg `0.0587` n `8`; equity avg `0.0179` n `158`; fx avg `-0.0007` n `6`; index avg `0.0096` n `27`; metal avg `0.0016` n `20`; unknown avg `0.1596` n `1262`
- 1h: commodity avg `0.0296` n `13`; crypto_alt avg `0.1359` n `239`; crypto_major avg `0.0114` n `8`; equity avg `0.0312` n `158`; fx avg `0.0064` n `6`; index avg `0.0118` n `27`; metal avg `-0.008` n `20`; unknown avg `-0.4508` n `1255`
- 4h: commodity avg `0.0823` n `13`; crypto_alt avg `-0.1193` n `239`; crypto_major avg `-0.1269` n `8`; equity avg `-0.1309` n `158`; fx avg `-0.0388` n `6`; index avg `0.0374` n `27`; metal avg `-0.0181` n `20`; unknown avg `160.4538` n `1241`
- 24h: commodity avg `0.1752` n `13`; crypto_alt avg `-1.8329` n `239`; crypto_major avg `-0.9565` n `8`; equity avg `-0.1238` n `158`; fx avg `0.0077` n `6`; index avg `-0.0321` n `27`; metal avg `0.0392` n `20`; unknown avg `-0.7328` n `1113`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
