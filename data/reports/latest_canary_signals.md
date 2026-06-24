# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T17:37:46.233896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8242` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.4586` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.2612` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8454` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4917` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.5193` n `228`; crypto_major avg `0.2582` n `8`; equity avg `-0.0914` n `86`; fx avg `-0.0119` n `6`; index avg `-0.0374` n `23`; metal avg `-0.1587` n `20`; unknown avg `1.4814` n `764`
- 1h: commodity avg `-0.0913` n `12`; crypto_alt avg `-2.4209` n `228`; crypto_major avg `-1.6582` n `8`; equity avg `-0.965` n `86`; fx avg `-0.0063` n `6`; index avg `-0.1665` n `23`; metal avg `-0.5287` n `20`; unknown avg `-0.8632` n `764`
- 4h: commodity avg `0.1488` n `12`; crypto_alt avg `-3.6538` n `228`; crypto_major avg `-3.6754` n `8`; equity avg `-1.83` n `86`; fx avg `0.0075` n `6`; index avg `-0.2168` n `23`; metal avg `-0.4142` n `20`; unknown avg `-0.3098` n `764`
- 24h: commodity avg `-0.4615` n `12`; crypto_alt avg `-4.6603` n `228`; crypto_major avg `-4.3724` n `8`; equity avg `1.2074` n `86`; fx avg `0.0583` n `6`; index avg `-0.1031` n `23`; metal avg `-1.9846` n `20`; unknown avg `-0.0944` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
