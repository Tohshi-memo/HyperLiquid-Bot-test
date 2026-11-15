# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T02:52:23.537009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `4.1336` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `4.0301` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.3721` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `3.3669` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.3218` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.7337` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.0179` n `239`; crypto_major avg `0.0486` n `8`; equity avg `0.0575` n `162`; fx avg `0.0079` n `6`; index avg `0.0023` n `27`; metal avg `0.0179` n `20`; unknown avg `0.1788` n `1263`
- 1h: commodity avg `0.0255` n `13`; crypto_alt avg `3.0178` n `239`; crypto_major avg `4.1591` n `8`; equity avg `0.7922` n `162`; fx avg `0.0045` n `6`; index avg `0.04` n `27`; metal avg `0.129` n `20`; unknown avg `58.6857` n `1257`
- 4h: commodity avg `0.0572` n `13`; crypto_alt avg `2.8611` n `239`; crypto_major avg `3.379` n `8`; equity avg `0.6453` n `162`; fx avg `0.0014` n `6`; index avg `0.0278` n `27`; metal avg `0.0069` n `20`; unknown avg `241.2436` n `1250`
- 24h: commodity avg `-0.0057` n `13`; crypto_alt avg `-6.0309` n `239`; crypto_major avg `-5.1897` n `8`; equity avg `-0.8857` n `162`; fx avg `0.0336` n `6`; index avg `-0.0797` n `27`; metal avg `-0.448` n `20`; unknown avg `47.2481` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
