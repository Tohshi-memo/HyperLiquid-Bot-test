# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T06:52:26.885533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.5525` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.4065` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.6553` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0132` n `13`; crypto_alt avg `1.9636` n `239`; crypto_major avg `2.4445` n `8`; equity avg `0.6677` n `166`; fx avg `-0.0008` n `6`; index avg `0.0483` n `27`; metal avg `0.1206` n `20`; unknown avg `1.1021` n `1262`
- 1h: commodity avg `0.0223` n `13`; crypto_alt avg `2.5486` n `239`; crypto_major avg `3.5748` n `8`; equity avg `0.9195` n `166`; fx avg `-0.0883` n `6`; index avg `0.0719` n `27`; metal avg `0.1683` n `20`; unknown avg `339.2102` n `1228`
- 4h: commodity avg `-0.0363` n `13`; crypto_alt avg `-0.8588` n `239`; crypto_major avg `-0.4458` n `8`; equity avg `-0.2522` n `166`; fx avg `-0.1157` n `6`; index avg `-0.0062` n `27`; metal avg `0.0019` n `20`; unknown avg `33.6396` n `1214`
- 24h: commodity avg `0.3997` n `13`; crypto_alt avg `-5.1015` n `239`; crypto_major avg `-6.2912` n `8`; equity avg `-4.7292` n `166`; fx avg `-0.1596` n `6`; index avg `-0.5027` n `27`; metal avg `-0.2526` n `20`; unknown avg `17.9536` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
