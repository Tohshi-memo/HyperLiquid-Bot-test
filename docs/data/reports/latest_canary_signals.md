# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T17:07:38.146440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.166` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0258` n `13`; crypto_alt avg `0.022` n `239`; crypto_major avg `-0.1727` n `8`; equity avg `-0.0368` n `160`; fx avg `-0.0025` n `6`; index avg `-0.003` n `27`; metal avg `0.0353` n `20`; unknown avg `0.3546` n `1257`
- 1h: commodity avg `-0.0701` n `13`; crypto_alt avg `-0.6009` n `239`; crypto_major avg `-0.5652` n `8`; equity avg `-0.2018` n `160`; fx avg `0.0035` n `6`; index avg `-0.0041` n `27`; metal avg `-0.1265` n `20`; unknown avg `-0.1445` n `1255`
- 4h: commodity avg `0.1749` n `13`; crypto_alt avg `0.22` n `239`; crypto_major avg `0.3005` n `8`; equity avg `3.4665` n `160`; fx avg `-0.0082` n `6`; index avg `0.3599` n `27`; metal avg `0.0015` n `20`; unknown avg `4.7454` n `1249`
- 24h: commodity avg `-0.3164` n `13`; crypto_alt avg `0.864` n `239`; crypto_major avg `-2.3662` n `8`; equity avg `4.0229` n `160`; fx avg `-0.1663` n `6`; index avg `0.4326` n `27`; metal avg `0.4243` n `20`; unknown avg `6.4474` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
