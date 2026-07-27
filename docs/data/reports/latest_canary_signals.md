# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T21:52:30.790742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.004` n `230`; crypto_major avg `-0.05` n `8`; equity avg `-0.0326` n `102`; fx avg `-0.0011` n `6`; index avg `0.0055` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0125` n `774`
- 1h: commodity avg `0.0827` n `12`; crypto_alt avg `-0.1582` n `230`; crypto_major avg `-0.2172` n `8`; equity avg `0.0498` n `102`; fx avg `-0.0125` n `6`; index avg `0.0036` n `25`; metal avg `0.0067` n `20`; unknown avg `3.8015` n `774`
- 4h: commodity avg `-0.0986` n `12`; crypto_alt avg `-0.0214` n `230`; crypto_major avg `-0.2546` n `8`; equity avg `0.8857` n `102`; fx avg `-0.0005` n `6`; index avg `0.1588` n `25`; metal avg `0.0239` n `20`; unknown avg `99.0979` n `774`
- 24h: commodity avg `-0.8657` n `12`; crypto_alt avg `-1.2518` n `230`; crypto_major avg `-0.7802` n `8`; equity avg `-1.0231` n `102`; fx avg `-0.0415` n `6`; index avg `-0.3202` n `25`; metal avg `0.1409` n `20`; unknown avg `97.592` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
