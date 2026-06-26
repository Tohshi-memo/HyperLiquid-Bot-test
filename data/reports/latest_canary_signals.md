# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T16:37:40.006890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.504` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9221` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.039` n `12`; crypto_alt avg `0.6795` n `228`; crypto_major avg `0.7369` n `8`; equity avg `0.3321` n `86`; fx avg `-0.0097` n `6`; index avg `0.0655` n `23`; metal avg `0.033` n `20`; unknown avg `-0.0527` n `765`
- 1h: commodity avg `0.0731` n `12`; crypto_alt avg `0.598` n `228`; crypto_major avg `0.3162` n `8`; equity avg `-0.0107` n `86`; fx avg `-0.0104` n `6`; index avg `0.0065` n `23`; metal avg `-0.0274` n `20`; unknown avg `-0.0508` n `765`
- 4h: commodity avg `-0.1448` n `12`; crypto_alt avg `2.2417` n `228`; crypto_major avg `2.3592` n `8`; equity avg `1.6268` n `86`; fx avg `-0.0432` n `6`; index avg `0.22` n `23`; metal avg `0.4371` n `20`; unknown avg `0.1848` n `765`
- 24h: commodity avg `-0.3567` n `12`; crypto_alt avg `2.662` n `228`; crypto_major avg `3.0291` n `8`; equity avg `-0.25` n `86`; fx avg `-0.0768` n `6`; index avg `-0.1882` n `23`; metal avg `0.616` n `20`; unknown avg `0.146` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
