# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T23:37:23.289324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `13`; crypto_alt avg `0.0807` n `239`; crypto_major avg `0.0917` n `8`; equity avg `0.0386` n `158`; fx avg `-0.0093` n `6`; index avg `-0.0015` n `27`; metal avg `0.0059` n `20`; unknown avg `0.076` n `1262`
- 1h: commodity avg `-0.0115` n `13`; crypto_alt avg `0.1014` n `239`; crypto_major avg `0.0828` n `8`; equity avg `0.1084` n `158`; fx avg `-0.0061` n `6`; index avg `0.0048` n `27`; metal avg `-0.0011` n `20`; unknown avg `-0.1355` n `1240`
- 4h: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.0892` n `239`; crypto_major avg `-0.084` n `8`; equity avg `-0.1008` n `158`; fx avg `-0.007` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.0863` n `1198`
- 24h: commodity avg `0.0688` n `13`; crypto_alt avg `-1.1531` n `239`; crypto_major avg `-0.6428` n `8`; equity avg `0.043` n `158`; fx avg `-0.0303` n `6`; index avg `0.0579` n `27`; metal avg `-0.0114` n `20`; unknown avg `160.3825` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
