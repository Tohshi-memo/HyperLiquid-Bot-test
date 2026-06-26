# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T17:22:31.869896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2624` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7063` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.1402` n `228`; crypto_major avg `-0.1762` n `8`; equity avg `-0.1306` n `86`; fx avg `0.0017` n `6`; index avg `-0.0297` n `23`; metal avg `-0.0083` n `20`; unknown avg `-0.0392` n `765`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.6305` n `228`; crypto_major avg `0.6162` n `8`; equity avg `0.3775` n `86`; fx avg `0.004` n `6`; index avg `0.0589` n `23`; metal avg `-0.0007` n `20`; unknown avg `0.0959` n `765`
- 4h: commodity avg `-0.1742` n `12`; crypto_alt avg `3.1056` n `228`; crypto_major avg `3.0882` n `8`; equity avg `2.1763` n `86`; fx avg `-0.0627` n `6`; index avg `0.2922` n `23`; metal avg `0.3819` n `20`; unknown avg `0.7367` n `765`
- 24h: commodity avg `-0.4433` n `12`; crypto_alt avg `2.2566` n `228`; crypto_major avg `2.3009` n `8`; equity avg `-0.1362` n `86`; fx avg `-0.056` n `6`; index avg `-0.1805` n `23`; metal avg `0.5647` n `20`; unknown avg `0.2916` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
