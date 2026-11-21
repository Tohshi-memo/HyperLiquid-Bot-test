# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T13:37:25.832034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.411` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2377` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.5466` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `0.9906` n `239`; crypto_major avg `1.305` n `8`; equity avg `0.4732` n `166`; fx avg `-0.0009` n `6`; index avg `0.0494` n `27`; metal avg `0.1114` n `20`; unknown avg `2.3399` n `1262`
- 1h: commodity avg `0.0217` n `13`; crypto_alt avg `1.2169` n `239`; crypto_major avg `1.6069` n `8`; equity avg `0.6857` n `166`; fx avg `0.0043` n `6`; index avg `0.0926` n `27`; metal avg `0.1485` n `20`; unknown avg `7.2028` n `1256`
- 4h: commodity avg `0.0424` n `13`; crypto_alt avg `2.3277` n `239`; crypto_major avg `3.4534` n `8`; equity avg `0.9068` n `166`; fx avg `0.0388` n `6`; index avg `0.1055` n `27`; metal avg `0.2157` n `20`; unknown avg `166.6331` n `1220`
- 24h: commodity avg `0.2838` n `13`; crypto_alt avg `-1.7965` n `239`; crypto_major avg `-1.5486` n `8`; equity avg `-2.4312` n `166`; fx avg `-0.1257` n `6`; index avg `-0.2608` n `27`; metal avg `-0.0528` n `20`; unknown avg `2.2809` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
