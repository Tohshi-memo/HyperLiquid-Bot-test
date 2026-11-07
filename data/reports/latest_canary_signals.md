# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T11:22:28.220589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `-0.1697` n `239`; crypto_major avg `-0.1269` n `8`; equity avg `0.0324` n `158`; fx avg `0.0015` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0096` n `20`; unknown avg `0.456` n `1261`
- 1h: commodity avg `0.0307` n `13`; crypto_alt avg `-0.2566` n `239`; crypto_major avg `-0.094` n `8`; equity avg `0.037` n `158`; fx avg `0.003` n `6`; index avg `0.0053` n `27`; metal avg `-0.0038` n `20`; unknown avg `0.0832` n `1255`
- 4h: commodity avg `0.0873` n `13`; crypto_alt avg `-0.9025` n `239`; crypto_major avg `-0.2722` n `8`; equity avg `0.1018` n `158`; fx avg `-0.004` n `6`; index avg `-0.0047` n `27`; metal avg `0.0002` n `20`; unknown avg `136.078` n `1199`
- 24h: commodity avg `-0.1153` n `13`; crypto_alt avg `-1.3883` n `239`; crypto_major avg `-0.4674` n `8`; equity avg `-0.2058` n `158`; fx avg `-0.0229` n `6`; index avg `0.0011` n `27`; metal avg `0.07` n `20`; unknown avg `7.6616` n `1059`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
