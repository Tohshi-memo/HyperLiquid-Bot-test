# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T09:52:28.498297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.0065` n `239`; crypto_major avg `0.0575` n `8`; equity avg `0.075` n `168`; fx avg `-0.0065` n `6`; index avg `0.0061` n `27`; metal avg `0.0169` n `20`; unknown avg `0.9504` n `1267`
- 1h: commodity avg `-0.0303` n `13`; crypto_alt avg `-0.1647` n `239`; crypto_major avg `0.0127` n `8`; equity avg `0.0391` n `168`; fx avg `-0.0044` n `6`; index avg `-0.0015` n `27`; metal avg `0.0164` n `20`; unknown avg `40.9429` n `1243`
- 4h: commodity avg `-0.0432` n `13`; crypto_alt avg `0.0366` n `239`; crypto_major avg `-0.2028` n `8`; equity avg `0.107` n `168`; fx avg `-0.004` n `6`; index avg `-0.0131` n `27`; metal avg `0.0414` n `20`; unknown avg `0.9703` n `1191`
- 24h: commodity avg `-0.6687` n `13`; crypto_alt avg `-3.3357` n `239`; crypto_major avg `-3.1458` n `8`; equity avg `-0.3823` n `168`; fx avg `-0.0939` n `6`; index avg `0.0365` n `27`; metal avg `-0.3147` n `20`; unknown avg `190.392` n `1089`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
