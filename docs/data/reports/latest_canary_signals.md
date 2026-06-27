# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T20:07:34.448981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5299` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5166` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.1817` n `228`; crypto_major avg `0.0333` n `8`; equity avg `0.048` n `88`; fx avg `0.0006` n `6`; index avg `0.0118` n `23`; metal avg `0.007` n `20`; unknown avg `0.0703` n `764`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `-0.6315` n `228`; crypto_major avg `-0.6483` n `8`; equity avg `-0.0954` n `88`; fx avg `0.0` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0294` n `20`; unknown avg `0.1444` n `764`
- 4h: commodity avg `-0.026` n `12`; crypto_alt avg `-1.4555` n `228`; crypto_major avg `-1.5822` n `8`; equity avg `-0.1941` n `88`; fx avg `0.0007` n `6`; index avg `-0.0523` n `23`; metal avg `-0.0656` n `20`; unknown avg `0.3891` n `764`
- 24h: commodity avg `0.2434` n `12`; crypto_alt avg `-0.8701` n `228`; crypto_major avg `-1.0382` n `8`; equity avg `0.4968` n `88`; fx avg `0.0874` n `6`; index avg `0.0319` n `23`; metal avg `0.0985` n `20`; unknown avg `-0.2889` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
