# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T16:07:30.288521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5477` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9359` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `0.5665` n `228`; crypto_major avg `0.4072` n `8`; equity avg `0.0125` n `86`; fx avg `-0.0147` n `6`; index avg `0.0076` n `23`; metal avg `0.0575` n `20`; unknown avg `0.1181` n `765`
- 1h: commodity avg `0.0933` n `12`; crypto_alt avg `1.0912` n `228`; crypto_major avg `1.0934` n `8`; equity avg `0.7073` n `86`; fx avg `0.007` n `6`; index avg `0.1193` n `23`; metal avg `0.1361` n `20`; unknown avg `0.097` n `765`
- 4h: commodity avg `-0.178` n `12`; crypto_alt avg `2.1478` n `228`; crypto_major avg `2.3697` n `8`; equity avg `1.4092` n `86`; fx avg `-0.0283` n `6`; index avg `0.179` n `23`; metal avg `0.4338` n `20`; unknown avg `0.4293` n `765`
- 24h: commodity avg `-0.4579` n `12`; crypto_alt avg `1.8409` n `228`; crypto_major avg `2.5779` n `8`; equity avg `-0.4605` n `86`; fx avg `-0.0465` n `6`; index avg `-0.2189` n `23`; metal avg `0.5195` n `20`; unknown avg `0.3471` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
