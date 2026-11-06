# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T04:37:27.260453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0654` n `13`; crypto_alt avg `0.2894` n `239`; crypto_major avg `0.263` n `8`; equity avg `0.2868` n `158`; fx avg `-0.0046` n `6`; index avg `0.0403` n `27`; metal avg `0.0412` n `20`; unknown avg `0.7679` n `1256`
- 1h: commodity avg `-0.093` n `13`; crypto_alt avg `0.3668` n `239`; crypto_major avg `0.1348` n `8`; equity avg `0.104` n `158`; fx avg `-0.041` n `6`; index avg `0.0075` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.0949` n `1244`
- 4h: commodity avg `0.2741` n `13`; crypto_alt avg `0.3069` n `239`; crypto_major avg `-0.5244` n `8`; equity avg `0.3966` n `158`; fx avg `-0.0458` n `6`; index avg `0.0824` n `27`; metal avg `-0.2913` n `20`; unknown avg `-0.3266` n `1244`
- 24h: commodity avg `1.5092` n `13`; crypto_alt avg `-4.4391` n `239`; crypto_major avg `-5.7923` n `8`; equity avg `-5.925` n `158`; fx avg `0.0046` n `6`; index avg `-0.7709` n `27`; metal avg `-0.5863` n `20`; unknown avg `230.7446` n `1033`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2396`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
