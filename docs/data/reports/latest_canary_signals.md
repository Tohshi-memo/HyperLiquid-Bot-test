# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T08:52:30.919406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `13`; crypto_alt avg `0.0822` n `239`; crypto_major avg `0.0306` n `8`; equity avg `0.2526` n `158`; fx avg `0.008` n `6`; index avg `0.0429` n `27`; metal avg `0.0543` n `20`; unknown avg `0.0741` n `1256`
- 1h: commodity avg `-0.2765` n `13`; crypto_alt avg `0.3722` n `239`; crypto_major avg `0.231` n `8`; equity avg `0.4648` n `158`; fx avg `0.0142` n `6`; index avg `0.0944` n `27`; metal avg `0.2169` n `20`; unknown avg `0.0571` n `1194`
- 4h: commodity avg `-0.2105` n `13`; crypto_alt avg `0.2435` n `239`; crypto_major avg `-0.2066` n `8`; equity avg `0.3647` n `158`; fx avg `-0.0861` n `6`; index avg `0.0581` n `27`; metal avg `0.2584` n `20`; unknown avg `0.1282` n `1166`
- 24h: commodity avg `0.9148` n `13`; crypto_alt avg `-4.3501` n `239`; crypto_major avg `-6.1047` n `8`; equity avg `-5.5509` n `158`; fx avg `-0.0328` n `6`; index avg `-0.685` n `27`; metal avg `-0.2204` n `20`; unknown avg `240.8735` n `991`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
