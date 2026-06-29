# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T09:37:28.198242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0669` n `12`; crypto_alt avg `-0.0602` n `228`; crypto_major avg `-0.1472` n `8`; equity avg `0.0355` n `88`; fx avg `0.0144` n `6`; index avg `0.0003` n `23`; metal avg `-0.0843` n `20`; unknown avg `-0.0133` n `764`
- 1h: commodity avg `0.0923` n `12`; crypto_alt avg `0.0694` n `228`; crypto_major avg `0.0151` n `8`; equity avg `-0.0666` n `88`; fx avg `-0.0076` n `6`; index avg `-0.0171` n `23`; metal avg `-0.2218` n `20`; unknown avg `-0.2098` n `764`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.5722` n `228`; crypto_major avg `0.5167` n `8`; equity avg `0.6136` n `88`; fx avg `0.0069` n `6`; index avg `0.1129` n `23`; metal avg `0.1063` n `20`; unknown avg `1.1828` n `732`
- 24h: commodity avg `-0.3418` n `12`; crypto_alt avg `-0.1014` n `228`; crypto_major avg `-0.4222` n `8`; equity avg `0.3516` n `88`; fx avg `0.0438` n `6`; index avg `0.0653` n `23`; metal avg `-0.3979` n `20`; unknown avg `-0.1906` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
