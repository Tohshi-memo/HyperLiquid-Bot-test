# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T01:37:20.380018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.2907` n `228`; crypto_major avg `0.0367` n `8`; equity avg `0.0799` n `74`; fx avg `-0.0023` n `6`; index avg `0.0673` n `23`; metal avg `0.0761` n `18`; unknown avg `0.0844` n `516`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `1.551` n `228`; crypto_major avg `1.1659` n `8`; equity avg `0.3845` n `74`; fx avg `0.0035` n `6`; index avg `0.1132` n `23`; metal avg `0.166` n `18`; unknown avg `0.8008` n `516`
- 4h: commodity avg `0.0577` n `12`; crypto_alt avg `2.3037` n `228`; crypto_major avg `1.6369` n `8`; equity avg `0.575` n `74`; fx avg `0.0035` n `6`; index avg `-0.0663` n `23`; metal avg `0.2364` n `18`; unknown avg `0.6209` n `515`
- 24h: commodity avg `0.1577` n `12`; crypto_alt avg `0.5367` n `228`; crypto_major avg `-0.155` n `8`; equity avg `0.4787` n `74`; fx avg `0.0353` n `6`; index avg `0.181` n `23`; metal avg `-0.156` n `18`; unknown avg `-0.088` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
