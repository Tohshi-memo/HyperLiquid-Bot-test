# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T16:22:39.160621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6735` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6342` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2977` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0829` n `12`; crypto_alt avg `0.4414` n `228`; crypto_major avg `0.4525` n `8`; equity avg `0.179` n `86`; fx avg `0.004` n `6`; index avg `0.021` n `23`; metal avg `0.0251` n `20`; unknown avg `0.653` n `764`
- 1h: commodity avg `0.1086` n `12`; crypto_alt avg `-0.6756` n `228`; crypto_major avg `-0.8906` n `8`; equity avg `-0.1933` n `86`; fx avg `-0.0119` n `6`; index avg `0.0044` n `23`; metal avg `-0.1033` n `20`; unknown avg `0.2631` n `764`
- 4h: commodity avg `-0.0401` n `12`; crypto_alt avg `-2.1838` n `228`; crypto_major avg `-2.7136` n `8`; equity avg `-1.4136` n `86`; fx avg `-0.0119` n `6`; index avg `-0.0794` n `23`; metal avg `-0.4159` n `20`; unknown avg `0.8244` n `764`
- 24h: commodity avg `-0.4725` n `12`; crypto_alt avg `-2.1962` n `228`; crypto_major avg `-2.5775` n `8`; equity avg `2.4045` n `86`; fx avg `0.0369` n `6`; index avg `0.0734` n `23`; metal avg `-1.711` n `20`; unknown avg `0.3255` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
