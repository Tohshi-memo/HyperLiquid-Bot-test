# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T21:37:32.361918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `13`; crypto_alt avg `0.0835` n `239`; crypto_major avg `-0.0052` n `8`; equity avg `0.0584` n `158`; fx avg `-0.008` n `6`; index avg `0.0366` n `27`; metal avg `-0.0573` n `20`; unknown avg `0.9962` n `1262`
- 1h: commodity avg `-0.0712` n `13`; crypto_alt avg `0.0255` n `239`; crypto_major avg `-0.1608` n `8`; equity avg `0.3953` n `158`; fx avg `-0.0145` n `6`; index avg `0.0689` n `27`; metal avg `-0.0542` n `20`; unknown avg `0.4574` n `1216`
- 4h: commodity avg `0.2595` n `13`; crypto_alt avg `-0.3391` n `239`; crypto_major avg `-0.3721` n `8`; equity avg `-0.1428` n `158`; fx avg `0.0004` n `6`; index avg `0.0061` n `27`; metal avg `-0.0359` n `20`; unknown avg `-0.2646` n `1194`
- 24h: commodity avg `-1.8376` n `13`; crypto_alt avg `1.1522` n `239`; crypto_major avg `1.3711` n `8`; equity avg `-1.5951` n `158`; fx avg `0.0436` n `6`; index avg `0.0814` n `27`; metal avg `1.229` n `20`; unknown avg `-0.2016` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
