# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T22:37:25.558211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.2575` n `228`; crypto_major avg `0.3313` n `8`; equity avg `0.0596` n `88`; fx avg `0.0` n `6`; index avg `0.0062` n `23`; metal avg `0.0223` n `20`; unknown avg `0.4867` n `764`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `0.0289` n `228`; crypto_major avg `0.0067` n `8`; equity avg `-0.0328` n `88`; fx avg `0.0037` n `6`; index avg `-0.0612` n `23`; metal avg `-0.0107` n `20`; unknown avg `0.2726` n `764`
- 4h: commodity avg `0.139` n `12`; crypto_alt avg `-0.6668` n `228`; crypto_major avg `-0.7507` n `8`; equity avg `-0.0284` n `88`; fx avg `0.0042` n `6`; index avg `-0.0393` n `23`; metal avg `-0.0265` n `20`; unknown avg `-0.3372` n `764`
- 24h: commodity avg `0.1683` n `12`; crypto_alt avg `-0.3291` n `228`; crypto_major avg `-0.5576` n `8`; equity avg `0.4209` n `88`; fx avg `0.0193` n `6`; index avg `-0.039` n `23`; metal avg `-0.0216` n `20`; unknown avg `-0.5685` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
