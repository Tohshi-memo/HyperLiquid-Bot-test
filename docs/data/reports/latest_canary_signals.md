# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T12:34:09.022161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.089` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9434` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `0.1984` n `231`; crypto_major avg `0.3415` n `8`; equity avg `-0.1165` n `122`; fx avg `-0.0029` n `6`; index avg `-0.031` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.0008` n `793`
- 1h: commodity avg `0.1351` n `12`; crypto_alt avg `-0.2078` n `231`; crypto_major avg `0.1249` n `8`; equity avg `-0.3164` n `122`; fx avg `-0.025` n `6`; index avg `-0.0707` n `25`; metal avg `-0.0876` n `20`; unknown avg `0.1059` n `793`
- 4h: commodity avg `0.2715` n `12`; crypto_alt avg `1.4996` n `231`; crypto_major avg `2.0545` n `8`; equity avg `-0.0345` n `122`; fx avg `-0.0409` n `6`; index avg `-0.0194` n `25`; metal avg `0.1111` n `20`; unknown avg `1.113` n `793`
- 24h: commodity avg `0.0717` n `12`; crypto_alt avg `1.2924` n `231`; crypto_major avg `1.0729` n `8`; equity avg `-1.6252` n `122`; fx avg `-0.1432` n `6`; index avg `-0.177` n `25`; metal avg `0.1648` n `20`; unknown avg `3.8758` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
