# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T00:22:28.445978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `0.1171` n `228`; crypto_major avg `0.0347` n `8`; equity avg `-0.0292` n `74`; fx avg `0.0002` n `6`; index avg `0.0133` n `23`; metal avg `0.0067` n `18`; unknown avg `24.2017` n `516`
- 1h: commodity avg `0.052` n `12`; crypto_alt avg `0.5268` n `228`; crypto_major avg `0.3436` n `8`; equity avg `0.2108` n `74`; fx avg `-0.0015` n `6`; index avg `0.0155` n `23`; metal avg `0.1038` n `18`; unknown avg `0.0164` n `515`
- 4h: commodity avg `0.1545` n `12`; crypto_alt avg `1.1023` n `228`; crypto_major avg `0.7008` n `8`; equity avg `0.3556` n `74`; fx avg `-0.0437` n `6`; index avg `0.1314` n `23`; metal avg `0.0844` n `18`; unknown avg `0.0602` n `515`
- 24h: commodity avg `0.2534` n `12`; crypto_alt avg `-1.4058` n `228`; crypto_major avg `-1.6498` n `8`; equity avg `-0.5551` n `74`; fx avg `0.0138` n `6`; index avg `-0.181` n `23`; metal avg `-0.3181` n `18`; unknown avg `0.7269` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
