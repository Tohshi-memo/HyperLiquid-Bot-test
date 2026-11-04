# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T22:22:32.116046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `0.28` n `239`; crypto_major avg `0.3332` n `8`; equity avg `-0.0716` n `158`; fx avg `0.0064` n `6`; index avg `0.0178` n `27`; metal avg `0.0095` n `20`; unknown avg `0.4763` n `1264`
- 1h: commodity avg `-0.0718` n `13`; crypto_alt avg `0.7536` n `239`; crypto_major avg `0.5182` n `8`; equity avg `0.1206` n `158`; fx avg `-0.0133` n `6`; index avg `0.016` n `27`; metal avg `-0.0574` n `20`; unknown avg `0.1009` n `1258`
- 4h: commodity avg `-0.235` n `13`; crypto_alt avg `0.3177` n `239`; crypto_major avg `-0.171` n `8`; equity avg `0.2403` n `158`; fx avg `-0.0052` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0261` n `20`; unknown avg `-0.7663` n `1194`
- 24h: commodity avg `-1.8936` n `13`; crypto_alt avg `2.0358` n `239`; crypto_major avg `2.1659` n `8`; equity avg `-1.3716` n `158`; fx avg `0.0626` n `6`; index avg `0.0717` n `27`; metal avg `1.2235` n `20`; unknown avg `-0.525` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2659`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
