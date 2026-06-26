# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T16:52:27.165992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5962` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2036` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0473` n `12`; crypto_alt avg `-0.3416` n `228`; crypto_major avg `-0.3137` n `8`; equity avg `-0.0401` n `86`; fx avg `0.0109` n `6`; index avg `0.0016` n `23`; metal avg `-0.0417` n `20`; unknown avg `0.2156` n `765`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `0.5928` n `228`; crypto_major avg `0.3298` n `8`; equity avg `0.0612` n `86`; fx avg `-0.0217` n `6`; index avg `0.0338` n `23`; metal avg `0.0129` n `20`; unknown avg `0.1629` n `765`
- 4h: commodity avg `-0.0107` n `12`; crypto_alt avg `2.5347` n `228`; crypto_major avg `2.5855` n `8`; equity avg `1.8381` n `86`; fx avg `-0.0499` n `6`; index avg `0.2659` n `23`; metal avg `0.3819` n `20`; unknown avg `0.5194` n `765`
- 24h: commodity avg `-0.3369` n `12`; crypto_alt avg `2.7497` n `228`; crypto_major avg `3.0952` n `8`; equity avg `-0.2171` n `86`; fx avg `-0.0616` n `6`; index avg `-0.1683` n `23`; metal avg `0.5773` n `20`; unknown avg `0.2199` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
