# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T07:07:40.170705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.7858` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.5965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.6829` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0165` n `13`; crypto_alt avg `-0.2489` n `239`; crypto_major avg `-0.0249` n `8`; equity avg `0.0458` n `166`; fx avg `0.003` n `6`; index avg `0.0161` n `27`; metal avg `-0.0132` n `20`; unknown avg `4.6462` n `1252`
- 1h: commodity avg `-0.0204` n `13`; crypto_alt avg `2.5564` n `239`; crypto_major avg `3.7654` n `8`; equity avg `1.0825` n `166`; fx avg `-0.0911` n `6`; index avg `0.0976` n `27`; metal avg `0.1689` n `20`; unknown avg `166.542` n `1248`
- 4h: commodity avg `-0.0551` n `13`; crypto_alt avg `-0.3458` n `239`; crypto_major avg `0.3333` n `8`; equity avg `-0.0652` n `166`; fx avg `-0.1125` n `6`; index avg `0.0212` n `27`; metal avg `0.0248` n `20`; unknown avg `7.4715` n `1208`
- 24h: commodity avg `0.3873` n `13`; crypto_alt avg `-5.2462` n `239`; crypto_major avg `-6.2658` n `8`; equity avg `-4.5731` n `166`; fx avg `-0.1643` n `6`; index avg `-0.4877` n `27`; metal avg `-0.1667` n `20`; unknown avg `23.138` n `1103`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
