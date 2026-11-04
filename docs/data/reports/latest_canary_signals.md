# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T17:07:44.476330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9579` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.5819` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.2149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.05` n `13`; crypto_alt avg `-0.3583` n `239`; crypto_major avg `-0.3248` n `8`; equity avg `0.0083` n `158`; fx avg `0.0163` n `6`; index avg `-0.0076` n `27`; metal avg `0.0725` n `20`; unknown avg `3.5969` n `1258`
- 1h: commodity avg `-0.8207` n `13`; crypto_alt avg `-0.1739` n `239`; crypto_major avg `-0.3361` n `8`; equity avg `0.8314` n `158`; fx avg `-0.0113` n `6`; index avg `0.1301` n `27`; metal avg `0.1676` n `20`; unknown avg `4.4128` n `1258`
- 4h: commodity avg `-1.4319` n `13`; crypto_alt avg `1.8042` n `239`; crypto_major avg `2.526` n `8`; equity avg `-0.0559` n `158`; fx avg `-0.0528` n `6`; index avg `0.1395` n `27`; metal avg `0.3111` n `20`; unknown avg `4.6878` n `1252`
- 24h: commodity avg `-1.5999` n `13`; crypto_alt avg `2.3082` n `239`; crypto_major avg `2.2419` n `8`; equity avg `-0.7865` n `158`; fx avg `0.0583` n `6`; index avg `0.1364` n `27`; metal avg `1.1688` n `20`; unknown avg `3.3929` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2659`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
