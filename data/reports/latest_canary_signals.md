# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T18:52:29.668292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.208` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `0.1005` n `239`; crypto_major avg `0.2849` n `8`; equity avg `0.6686` n `168`; fx avg `0.0056` n `6`; index avg `0.0865` n `27`; metal avg `0.1325` n `20`; unknown avg `238.8946` n `1267`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `0.4508` n `239`; crypto_major avg `0.7041` n `8`; equity avg `1.8259` n `168`; fx avg `0.0237` n `6`; index avg `0.1904` n `27`; metal avg `0.3824` n `20`; unknown avg `1.2606` n `1263`
- 4h: commodity avg `0.1925` n `13`; crypto_alt avg `3.7018` n `239`; crypto_major avg `4.1183` n `8`; equity avg `5.0546` n `168`; fx avg `0.1045` n `6`; index avg `0.5568` n `27`; metal avg `0.9103` n `20`; unknown avg `49.7978` n `1253`
- 24h: commodity avg `0.2842` n `13`; crypto_alt avg `0.9313` n `239`; crypto_major avg `0.2255` n `8`; equity avg `-1.0517` n `168`; fx avg `0.0292` n `6`; index avg `-0.0854` n `27`; metal avg `-0.0722` n `20`; unknown avg `26.3511` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
