# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T15:52:37.372403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1187` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7191` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `0.0212` n `234`; crypto_major avg `-0.0923` n `8`; equity avg `0.1598` n `141`; fx avg `-0.0062` n `6`; index avg `0.0116` n `26`; metal avg `0.052` n `20`; unknown avg `5.2206` n `943`
- 1h: commodity avg `0.4289` n `12`; crypto_alt avg `1.5248` n `234`; crypto_major avg `1.1917` n `8`; equity avg `0.0545` n `141`; fx avg `0.0144` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0154` n `20`; unknown avg `1.3825` n `895`
- 4h: commodity avg `0.8341` n `12`; crypto_alt avg `3.4559` n `234`; crypto_major avg `2.0479` n `8`; equity avg `0.3288` n `141`; fx avg `0.0008` n `6`; index avg `0.0062` n `26`; metal avg `-0.0708` n `20`; unknown avg `3.5621` n `889`
- 24h: commodity avg `1.1311` n `12`; crypto_alt avg `3.1636` n `234`; crypto_major avg `1.2103` n `8`; equity avg `-1.1045` n `141`; fx avg `0.0259` n `6`; index avg `-0.2312` n `26`; metal avg `-0.1437` n `20`; unknown avg `262.8513` n `825`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
