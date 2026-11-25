# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T20:52:31.892649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3607` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2878` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.827` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.063` n `13`; crypto_alt avg `0.1426` n `239`; crypto_major avg `0.3013` n `8`; equity avg `0.6642` n `168`; fx avg `-0.0075` n `6`; index avg `0.0755` n `27`; metal avg `0.111` n `20`; unknown avg `8.8928` n `1255`
- 1h: commodity avg `0.0935` n `13`; crypto_alt avg `-0.0374` n `239`; crypto_major avg `0.1581` n `8`; equity avg `-0.1307` n `168`; fx avg `-0.0058` n `6`; index avg `-0.009` n `27`; metal avg `0.2053` n `20`; unknown avg `7.7989` n `1239`
- 4h: commodity avg `0.2052` n `13`; crypto_alt avg `3.3329` n `239`; crypto_major avg `3.5659` n `8`; equity avg `5.3929` n `168`; fx avg `0.0489` n `6`; index avg `0.5456` n `27`; metal avg `1.2781` n `20`; unknown avg `204.2879` n `1240`
- 24h: commodity avg `0.4048` n `13`; crypto_alt avg `1.8584` n `239`; crypto_major avg `1.0886` n `8`; equity avg `-1.0825` n `168`; fx avg `0.0442` n `6`; index avg `-0.1307` n `27`; metal avg `0.1682` n `20`; unknown avg `4.6194` n `1077`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
