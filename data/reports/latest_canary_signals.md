# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T23:37:34.037071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0259` n `234`; crypto_major avg `-0.0671` n `8`; equity avg `0.0361` n `142`; fx avg `-0.0011` n `6`; index avg `0.0204` n `26`; metal avg `0.0021` n `20`; unknown avg `0.7958` n `975`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0455` n `234`; crypto_major avg `-0.1236` n `8`; equity avg `0.0539` n `142`; fx avg `0.0064` n `6`; index avg `0.0396` n `26`; metal avg `-0.019` n `20`; unknown avg `1.2587` n `973`
- 4h: commodity avg `-0.1182` n `12`; crypto_alt avg `0.4635` n `234`; crypto_major avg `0.2596` n `8`; equity avg `0.0397` n `142`; fx avg `0.0317` n `6`; index avg `0.0249` n `26`; metal avg `-0.0108` n `20`; unknown avg `2.3491` n `887`
- 24h: commodity avg `0.1844` n `12`; crypto_alt avg `1.1254` n `234`; crypto_major avg `0.942` n `8`; equity avg `-0.3295` n `142`; fx avg `0.1002` n `6`; index avg `-0.0052` n `26`; metal avg `-0.2676` n `20`; unknown avg `759.7621` n `813`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
