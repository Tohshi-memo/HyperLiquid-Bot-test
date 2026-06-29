# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T08:22:35.953012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0664` n `12`; crypto_alt avg `-0.0745` n `228`; crypto_major avg `0.0206` n `8`; equity avg `0.0221` n `88`; fx avg `0.0068` n `6`; index avg `0.0092` n `23`; metal avg `-0.0052` n `20`; unknown avg `-0.3176` n `764`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.1929` n `228`; crypto_major avg `-0.1283` n `8`; equity avg `0.2111` n `88`; fx avg `0.0122` n `6`; index avg `0.0289` n `23`; metal avg `0.0065` n `20`; unknown avg `1.0387` n `764`
- 4h: commodity avg `-0.1465` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `0.1565` n `8`; equity avg `0.7726` n `88`; fx avg `0.0196` n `6`; index avg `0.2204` n `23`; metal avg `0.0091` n `20`; unknown avg `1.1446` n `732`
- 24h: commodity avg `-0.4872` n `12`; crypto_alt avg `0.1856` n `228`; crypto_major avg `-0.0455` n `8`; equity avg `0.5774` n `88`; fx avg `0.0677` n `6`; index avg `0.1013` n `23`; metal avg `-0.1727` n `20`; unknown avg `-0.4131` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
