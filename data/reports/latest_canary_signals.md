# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T05:37:26.283607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.0478` n `228`; crypto_major avg `-0.1315` n `8`; equity avg `-0.0024` n `88`; fx avg `-0.0029` n `6`; index avg `0.0007` n `23`; metal avg `0.0019` n `20`; unknown avg `-0.3647` n `764`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.3989` n `228`; crypto_major avg `-0.3254` n `8`; equity avg `-0.0252` n `88`; fx avg `0.0053` n `6`; index avg `-0.0111` n `23`; metal avg `-0.0152` n `20`; unknown avg `0.9009` n `764`
- 4h: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.011` n `228`; crypto_major avg `0.2554` n `8`; equity avg `0.077` n `88`; fx avg `0.0046` n `6`; index avg `0.0039` n `23`; metal avg `-0.0044` n `20`; unknown avg `-1.3847` n `764`
- 24h: commodity avg `-0.1602` n `12`; crypto_alt avg `1.7272` n `228`; crypto_major avg `1.5391` n `8`; equity avg `1.5724` n `87`; fx avg `0.0068` n `6`; index avg `0.0479` n `23`; metal avg `1.0824` n `20`; unknown avg `-0.5167` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
