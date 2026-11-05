# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T11:07:27.018042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `13`; crypto_alt avg `-0.0337` n `239`; crypto_major avg `-0.0472` n `8`; equity avg `-0.2005` n `158`; fx avg `-0.0005` n `6`; index avg `-0.0009` n `27`; metal avg `0.0112` n `20`; unknown avg `1.0271` n `1247`
- 1h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.4184` n `239`; crypto_major avg `-0.2312` n `8`; equity avg `-0.2049` n `158`; fx avg `0.0169` n `6`; index avg `-0.002` n `27`; metal avg `0.0799` n `20`; unknown avg `8.864` n `1235`
- 4h: commodity avg `0.4715` n `13`; crypto_alt avg `-0.3642` n `239`; crypto_major avg `-0.235` n `8`; equity avg `-0.272` n `158`; fx avg `-0.0258` n `6`; index avg `0.005` n `27`; metal avg `0.0234` n `20`; unknown avg `10.4259` n `1133`
- 24h: commodity avg `-1.2465` n `13`; crypto_alt avg `0.258` n `239`; crypto_major avg `1.2774` n `8`; equity avg `-3.6461` n `158`; fx avg `-0.0163` n `6`; index avg `-0.3012` n `27`; metal avg `0.5791` n `20`; unknown avg `10.3545` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2462`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
