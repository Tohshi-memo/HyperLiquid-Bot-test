# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T14:37:35.339009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `13`; crypto_alt avg `0.2526` n `239`; crypto_major avg `0.3863` n `8`; equity avg `0.2085` n `158`; fx avg `0.0025` n `6`; index avg `0.0299` n `27`; metal avg `0.0957` n `20`; unknown avg `1.902` n `1264`
- 1h: commodity avg `-0.2529` n `13`; crypto_alt avg `0.1519` n `239`; crypto_major avg `0.4647` n `8`; equity avg `0.0907` n `158`; fx avg `-0.0023` n `6`; index avg `0.0669` n `27`; metal avg `0.1094` n `20`; unknown avg `20.0593` n `1258`
- 4h: commodity avg `-0.4527` n `13`; crypto_alt avg `-0.5115` n `239`; crypto_major avg `-0.2477` n `8`; equity avg `-1.6719` n `158`; fx avg `0.0263` n `6`; index avg `-0.037` n `27`; metal avg `-0.0358` n `20`; unknown avg `2.2721` n `1254`
- 24h: commodity avg `-0.5786` n `13`; crypto_alt avg `0.7999` n `239`; crypto_major avg `0.4037` n `8`; equity avg `0.0815` n `158`; fx avg `0.1557` n `6`; index avg `0.0919` n `27`; metal avg `0.786` n `20`; unknown avg `1.2654` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2585`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
