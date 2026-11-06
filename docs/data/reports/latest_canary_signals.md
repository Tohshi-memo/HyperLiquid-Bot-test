# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T04:22:31.150360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `-0.0016` n `239`; crypto_major avg `-0.1144` n `8`; equity avg `0.0044` n `158`; fx avg `-0.0036` n `6`; index avg `0.0187` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.1128` n `1256`
- 1h: commodity avg `0.1249` n `13`; crypto_alt avg `-0.301` n `239`; crypto_major avg `-0.4847` n `8`; equity avg `-0.323` n `158`; fx avg `-0.0586` n `6`; index avg `-0.0447` n `27`; metal avg `-0.1005` n `20`; unknown avg `-0.5276` n `1246`
- 4h: commodity avg `0.3758` n `13`; crypto_alt avg `0.6163` n `239`; crypto_major avg `-0.447` n `8`; equity avg `0.9498` n `158`; fx avg `-0.0403` n `6`; index avg `0.1484` n `27`; metal avg `-0.3152` n `20`; unknown avg `-0.1117` n `1242`
- 24h: commodity avg `1.5733` n `13`; crypto_alt avg `-4.4987` n `239`; crypto_major avg `-5.6802` n `8`; equity avg `-6.0327` n `158`; fx avg `0.0035` n `6`; index avg `-0.7787` n `27`; metal avg `-0.5876` n `20`; unknown avg `230.4277` n `1033`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
