# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T15:52:26.727038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `13`; crypto_alt avg `0.1493` n `239`; crypto_major avg `0.02` n `8`; equity avg `-0.0144` n `166`; fx avg `0.0082` n `6`; index avg `-0.0052` n `27`; metal avg `0.0094` n `20`; unknown avg `158.3326` n `1263`
- 1h: commodity avg `-0.0253` n `13`; crypto_alt avg `0.1019` n `239`; crypto_major avg `0.1875` n `8`; equity avg `-0.0173` n `166`; fx avg `0.0032` n `6`; index avg `-0.0017` n `27`; metal avg `0.0156` n `20`; unknown avg `1.1266` n `1259`
- 4h: commodity avg `-0.065` n `13`; crypto_alt avg `-0.068` n `239`; crypto_major avg `0.0229` n `8`; equity avg `-0.0718` n `166`; fx avg `0.0091` n `6`; index avg `0.0396` n `27`; metal avg `0.0318` n `20`; unknown avg `0.9183` n `1241`
- 24h: commodity avg `-0.0187` n `13`; crypto_alt avg `0.5684` n `239`; crypto_major avg `1.1552` n `8`; equity avg `0.937` n `166`; fx avg `-0.0137` n `6`; index avg `0.1656` n `27`; metal avg `0.0654` n `20`; unknown avg `0.1285` n `1080`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
