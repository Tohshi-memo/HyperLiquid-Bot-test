# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T02:07:29.181946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `-0.0588` n `239`; crypto_major avg `-0.1175` n `8`; equity avg `0.1455` n `158`; fx avg `0.0077` n `6`; index avg `0.04` n `27`; metal avg `-0.0566` n `20`; unknown avg `-0.1452` n `1250`
- 1h: commodity avg `0.13` n `13`; crypto_alt avg `-0.0719` n `239`; crypto_major avg `-0.227` n `8`; equity avg `0.5293` n `158`; fx avg `-0.006` n `6`; index avg `0.107` n `27`; metal avg `-0.0942` n `20`; unknown avg `-0.2207` n `1254`
- 4h: commodity avg `0.0362` n `13`; crypto_alt avg `0.659` n `239`; crypto_major avg `0.2468` n `8`; equity avg `1.5836` n `158`; fx avg `-0.0095` n `6`; index avg `0.2501` n `27`; metal avg `-0.0404` n `20`; unknown avg `1.1238` n `1216`
- 24h: commodity avg `1.3531` n `13`; crypto_alt avg `-4.7051` n `239`; crypto_major avg `-5.6929` n `8`; equity avg `-6.4529` n `158`; fx avg `0.0539` n `6`; index avg `-0.9193` n `27`; metal avg `-0.4918` n `20`; unknown avg `231.5776` n `1035`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2349`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
