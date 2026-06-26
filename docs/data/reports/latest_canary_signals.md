# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T17:13:02.925578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3987` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8535` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0622` n `12`; crypto_alt avg `0.4364` n `228`; crypto_major avg `0.3719` n `8`; equity avg `0.2166` n `86`; fx avg `0.0011` n `6`; index avg `0.0215` n `23`; metal avg `0.0163` n `20`; unknown avg `0.0636` n `765`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `0.4626` n `228`; crypto_major avg `0.2945` n `8`; equity avg `0.266` n `86`; fx avg `-0.006` n `6`; index avg `0.0477` n `23`; metal avg `-0.0283` n `20`; unknown avg `0.0288` n `765`
- 4h: commodity avg `-0.1384` n `12`; crypto_alt avg `3.1181` n `228`; crypto_major avg `3.2603` n `8`; equity avg `2.2844` n `86`; fx avg `-0.0702` n `6`; index avg `0.317` n `23`; metal avg `0.4068` n `20`; unknown avg `0.8732` n `765`
- 24h: commodity avg `-0.3891` n `12`; crypto_alt avg `3.1968` n `228`; crypto_major avg `3.4551` n `8`; equity avg `0.0767` n `86`; fx avg `-0.0567` n `6`; index avg `-0.1448` n `23`; metal avg `0.5821` n `20`; unknown avg `0.4104` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
