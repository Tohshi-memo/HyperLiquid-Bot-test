# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T01:22:35.320247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0685` n `12`; crypto_alt avg `0.0847` n `228`; crypto_major avg `0.1823` n `8`; equity avg `0.0266` n `88`; fx avg `-0.0044` n `6`; index avg `0.0026` n `23`; metal avg `-0.006` n `20`; unknown avg `0.105` n `764`
- 1h: commodity avg `0.2119` n `12`; crypto_alt avg `-0.0902` n `228`; crypto_major avg `-0.0799` n `8`; equity avg `-0.1084` n `88`; fx avg `-0.0096` n `6`; index avg `-0.0446` n `23`; metal avg `-0.0192` n `20`; unknown avg `24.6` n `764`
- 4h: commodity avg `0.5323` n `12`; crypto_alt avg `-0.4545` n `228`; crypto_major avg `-0.6861` n `8`; equity avg `-0.1536` n `88`; fx avg `-0.0234` n `6`; index avg `-0.1051` n `23`; metal avg `0.0161` n `20`; unknown avg `-0.6849` n `764`
- 24h: commodity avg `0.4478` n `12`; crypto_alt avg `-0.6886` n `228`; crypto_major avg `-0.8982` n `8`; equity avg `0.1589` n `88`; fx avg `-0.0024` n `6`; index avg `-0.1211` n `23`; metal avg `-0.0538` n `20`; unknown avg `-0.7299` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
