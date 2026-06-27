# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T16:46:32.834243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0972` n `228`; crypto_major avg `0.005` n `8`; equity avg `0.0047` n `88`; fx avg `-0.0032` n `6`; index avg `0.0039` n `23`; metal avg `0.0059` n `20`; unknown avg `-0.0017` n `764`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.0743` n `228`; crypto_major avg `-0.1` n `8`; equity avg `-0.0605` n `88`; fx avg `0.0068` n `6`; index avg `-0.0386` n `23`; metal avg `-0.0035` n `20`; unknown avg `0.0052` n `764`
- 4h: commodity avg `-0.0776` n `12`; crypto_alt avg `0.8084` n `228`; crypto_major avg `0.8177` n `8`; equity avg `0.0746` n `88`; fx avg `-0.001` n `6`; index avg `-0.0024` n `23`; metal avg `0.0103` n `20`; unknown avg `0.088` n `764`
- 24h: commodity avg `0.1627` n `12`; crypto_alt avg `0.7684` n `228`; crypto_major avg `0.6949` n `8`; equity avg `0.4639` n `87`; fx avg `0.0735` n `6`; index avg `-0.1391` n `23`; metal avg `-0.0035` n `20`; unknown avg `0.2972` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
