# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T00:22:30.544836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0441` n `13`; crypto_alt avg `0.1446` n `239`; crypto_major avg `0.358` n `8`; equity avg `0.084` n `158`; fx avg `0.011` n `6`; index avg `-0.015` n `27`; metal avg `0.1088` n `20`; unknown avg `-0.1247` n `1264`
- 1h: commodity avg `-0.0548` n `13`; crypto_alt avg `-0.1615` n `239`; crypto_major avg `0.2754` n `8`; equity avg `-0.3389` n `158`; fx avg `0.0141` n `6`; index avg `-0.1202` n `27`; metal avg `0.0906` n `20`; unknown avg `0.6054` n `1250`
- 4h: commodity avg `-0.1689` n `13`; crypto_alt avg `0.3011` n `239`; crypto_major avg `0.505` n `8`; equity avg `-0.1809` n `158`; fx avg `0.0143` n `6`; index avg `-0.0841` n `27`; metal avg `0.0544` n `20`; unknown avg `0.6657` n `1154`
- 24h: commodity avg `-1.8257` n `13`; crypto_alt avg `2.5784` n `239`; crypto_major avg `3.3969` n `8`; equity avg `-1.16` n `158`; fx avg `0.0538` n `6`; index avg `0.0716` n `27`; metal avg `1.2953` n `20`; unknown avg `30.8862` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2648`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
