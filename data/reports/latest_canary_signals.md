# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T22:07:30.720435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.2836` n `228`; crypto_major avg `-0.2786` n `8`; equity avg `0.0202` n `88`; fx avg `-0.0241` n `6`; index avg `0.0006` n `23`; metal avg `-0.0078` n `20`; unknown avg `-0.2149` n `764`
- 1h: commodity avg `-0.0244` n `12`; crypto_alt avg `0.0589` n `228`; crypto_major avg `0.1524` n `8`; equity avg `0.1796` n `88`; fx avg `0.0277` n `6`; index avg `0.0191` n `23`; metal avg `0.0094` n `20`; unknown avg `-0.0098` n `764`
- 4h: commodity avg `0.1013` n `12`; crypto_alt avg `-0.6369` n `228`; crypto_major avg `-0.7174` n `8`; equity avg `-0.0689` n `88`; fx avg `0.0592` n `6`; index avg `-0.1429` n `23`; metal avg `0.0111` n `20`; unknown avg `-0.604` n `764`
- 24h: commodity avg `-0.2913` n `12`; crypto_alt avg `1.2185` n `228`; crypto_major avg `1.0994` n `8`; equity avg `-0.2638` n `87`; fx avg `0.0046` n `6`; index avg `-0.3171` n `23`; metal avg `0.7179` n `20`; unknown avg `-0.5544` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
