# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T07:52:35.157177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.05` n `228`; crypto_major avg `0.0274` n `8`; equity avg `0.0388` n `88`; fx avg `0.0052` n `6`; index avg `0.0174` n `23`; metal avg `0.0622` n `20`; unknown avg `-0.0243` n `764`
- 1h: commodity avg `-0.2179` n `12`; crypto_alt avg `0.079` n `228`; crypto_major avg `0.0384` n `8`; equity avg `-0.0128` n `88`; fx avg `0.0159` n `6`; index avg `0.0481` n `23`; metal avg `-0.0491` n `20`; unknown avg `-0.0397` n `764`
- 4h: commodity avg `-0.2384` n `12`; crypto_alt avg `-0.0087` n `228`; crypto_major avg `-0.003` n `8`; equity avg `0.4215` n `88`; fx avg `0.0256` n `6`; index avg `0.1713` n `23`; metal avg `-0.0698` n `20`; unknown avg `-0.0074` n `732`
- 24h: commodity avg `-0.6018` n `12`; crypto_alt avg `0.4457` n `228`; crypto_major avg `0.2701` n `8`; equity avg `0.4087` n `88`; fx avg `0.0575` n `6`; index avg `0.1233` n `23`; metal avg `-0.1253` n `20`; unknown avg `-0.5594` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
