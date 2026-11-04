# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T11:22:32.859086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0914` n `13`; crypto_alt avg `0.3425` n `239`; crypto_major avg `0.0969` n `8`; equity avg `-0.1106` n `158`; fx avg `-0.0001` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0383` n `20`; unknown avg `1.3569` n `1258`
- 1h: commodity avg `0.0804` n `13`; crypto_alt avg `0.4062` n `239`; crypto_major avg `0.1986` n `8`; equity avg `0.0247` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0086` n `27`; metal avg `-0.0794` n `20`; unknown avg `1.0222` n `1258`
- 4h: commodity avg `-0.2426` n `13`; crypto_alt avg `0.6559` n `239`; crypto_major avg `0.7834` n `8`; equity avg `1.41` n `158`; fx avg `0.0506` n `6`; index avg `0.2457` n `27`; metal avg `0.2503` n `20`; unknown avg `18.8749` n `1166`
- 24h: commodity avg `-0.6728` n `13`; crypto_alt avg `2.3846` n `239`; crypto_major avg `1.7162` n `8`; equity avg `2.8477` n `158`; fx avg `0.1376` n `6`; index avg `0.2776` n `27`; metal avg `1.1248` n `20`; unknown avg `17.7837` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2597`, n `670`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1697`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1689`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1624`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1565`, n `670`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1475`, n `670`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `670`, weak_sample_signal
