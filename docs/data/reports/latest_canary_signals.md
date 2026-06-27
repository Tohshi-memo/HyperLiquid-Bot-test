# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T12:52:27.680248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0292` n `228`; crypto_major avg `0.1086` n `8`; equity avg `-0.0097` n `88`; fx avg `0.0` n `6`; index avg `-0.0007` n `23`; metal avg `0.0021` n `20`; unknown avg `0.0698` n `764`
- 1h: commodity avg `0.0388` n `12`; crypto_alt avg `0.1314` n `228`; crypto_major avg `0.1031` n `8`; equity avg `0.0121` n `88`; fx avg `0.0011` n `6`; index avg `0.0018` n `23`; metal avg `0.0011` n `20`; unknown avg `0.1129` n `764`
- 4h: commodity avg `0.1259` n `12`; crypto_alt avg `0.055` n `228`; crypto_major avg `-0.0942` n `8`; equity avg `-0.0013` n `88`; fx avg `0.0003` n `6`; index avg `-0.0157` n `23`; metal avg `-0.0119` n `20`; unknown avg `0.0887` n `764`
- 24h: commodity avg `0.2262` n `12`; crypto_alt avg `2.5042` n `228`; crypto_major avg `2.4509` n `8`; equity avg `2.2153` n `87`; fx avg `0.0245` n `6`; index avg `0.1263` n `23`; metal avg `0.3678` n `20`; unknown avg `0.4341` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
