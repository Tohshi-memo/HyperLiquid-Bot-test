# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T17:22:36.484064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0175` n `13`; crypto_alt avg `-0.1449` n `238`; crypto_major avg `-0.0357` n `8`; equity avg `-0.1175` n `155`; fx avg `-0.0083` n `6`; index avg `-0.0362` n `27`; metal avg `-0.0111` n `20`; unknown avg `1.1196` n `1238`
- 1h: commodity avg `-0.1234` n `13`; crypto_alt avg `-0.2691` n `238`; crypto_major avg `0.0129` n `8`; equity avg `-0.0319` n `155`; fx avg `0.0019` n `6`; index avg `-0.012` n `27`; metal avg `-0.0088` n `20`; unknown avg `2.1364` n `1232`
- 4h: commodity avg `0.1599` n `13`; crypto_alt avg `-0.4595` n `238`; crypto_major avg `-0.3041` n `8`; equity avg `0.1052` n `155`; fx avg `0.1109` n `6`; index avg `0.0243` n `27`; metal avg `-0.1327` n `20`; unknown avg `5.864` n `1150`
- 24h: commodity avg `0.5869` n `13`; crypto_alt avg `-0.4704` n `238`; crypto_major avg `-0.2969` n `8`; equity avg `0.9708` n `154`; fx avg `0.2494` n `6`; index avg `0.2514` n `27`; metal avg `-0.1917` n `20`; unknown avg `4.0266` n `1100`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
