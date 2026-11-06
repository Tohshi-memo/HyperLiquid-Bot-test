# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T09:37:25.215093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.0536` n `239`; crypto_major avg `0.0137` n `8`; equity avg `0.24` n `158`; fx avg `-0.006` n `6`; index avg `0.0511` n `27`; metal avg `-0.0387` n `20`; unknown avg `0.0933` n `1256`
- 1h: commodity avg `-0.1638` n `13`; crypto_alt avg `0.4251` n `239`; crypto_major avg `0.6334` n `8`; equity avg `1.5538` n `158`; fx avg `-0.0232` n `6`; index avg `0.1964` n `27`; metal avg `0.0575` n `20`; unknown avg `31.2191` n `1250`
- 4h: commodity avg `-0.3451` n `13`; crypto_alt avg `0.7712` n `239`; crypto_major avg `0.5923` n `8`; equity avg `1.7415` n `158`; fx avg `-0.1321` n `6`; index avg `0.1844` n `27`; metal avg `0.271` n `20`; unknown avg `17.5951` n `1172`
- 24h: commodity avg `0.6514` n `13`; crypto_alt avg `-3.8606` n `239`; crypto_major avg `-5.4092` n `8`; equity avg `-4.5331` n `158`; fx avg `-0.0421` n `6`; index avg `-0.5833` n `27`; metal avg `-0.2266` n `20`; unknown avg `229.3874` n `1063`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2198`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
