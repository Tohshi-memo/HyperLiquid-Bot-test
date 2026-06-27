# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T14:22:31.736745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.2083` n `228`; crypto_major avg `0.1378` n `8`; equity avg `0.0217` n `88`; fx avg `-0.0021` n `6`; index avg `0.0057` n `23`; metal avg `0.0017` n `20`; unknown avg `0.0044` n `764`
- 1h: commodity avg `0.0216` n `12`; crypto_alt avg `0.3678` n `228`; crypto_major avg `0.3361` n `8`; equity avg `0.0762` n `88`; fx avg `-0.0015` n `6`; index avg `0.006` n `23`; metal avg `0.0098` n `20`; unknown avg `0.0384` n `764`
- 4h: commodity avg `0.0988` n `12`; crypto_alt avg `0.668` n `228`; crypto_major avg `0.58` n `8`; equity avg `0.1509` n `88`; fx avg `-0.001` n `6`; index avg `0.0057` n `23`; metal avg `0.011` n `20`; unknown avg `0.306` n `764`
- 24h: commodity avg `0.3201` n `12`; crypto_alt avg `1.4222` n `228`; crypto_major avg `1.0007` n `8`; equity avg `0.6506` n `87`; fx avg `0.0287` n `6`; index avg `-0.0986` n `23`; metal avg `-0.0759` n `20`; unknown avg `0.252` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
