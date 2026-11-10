# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T01:37:33.679268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.067` n `13`; crypto_alt avg `-0.1079` n `239`; crypto_major avg `-0.1764` n `8`; equity avg `-0.0429` n `160`; fx avg `0.0153` n `6`; index avg `-0.005` n `27`; metal avg `-0.0545` n `20`; unknown avg `0.0189` n `1261`
- 1h: commodity avg `-0.1433` n `13`; crypto_alt avg `0.0082` n `239`; crypto_major avg `0.0587` n `8`; equity avg `-0.485` n `160`; fx avg `0.0197` n `6`; index avg `-0.052` n `27`; metal avg `0.0795` n `20`; unknown avg `0.5042` n `1253`
- 4h: commodity avg `-0.1343` n `13`; crypto_alt avg `-0.5694` n `239`; crypto_major avg `-0.0015` n `8`; equity avg `-0.3994` n `160`; fx avg `0.0773` n `6`; index avg `-0.1101` n `27`; metal avg `-0.0397` n `20`; unknown avg `19.4382` n `1241`
- 24h: commodity avg `-0.4545` n `13`; crypto_alt avg `0.8655` n `239`; crypto_major avg `-0.1022` n `8`; equity avg `4.3106` n `160`; fx avg `-0.0265` n `6`; index avg `0.4091` n `27`; metal avg `0.1978` n `20`; unknown avg `5.0658` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
