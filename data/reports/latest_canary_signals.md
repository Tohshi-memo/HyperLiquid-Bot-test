# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T00:52:25.841526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `0.2314` n `228`; crypto_major avg `0.222` n `8`; equity avg `-0.0312` n `88`; fx avg `0.0066` n `6`; index avg `-0.0008` n `23`; metal avg `0.0004` n `20`; unknown avg `1.0875` n `764`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `0.0261` n `228`; crypto_major avg `-0.2208` n `8`; equity avg `-0.0804` n `88`; fx avg `0.0123` n `6`; index avg `0.004` n `23`; metal avg `-0.0123` n `20`; unknown avg `0.7971` n `764`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `0.1493` n `228`; crypto_major avg `0.1551` n `8`; equity avg `0.2055` n `88`; fx avg `0.0577` n `6`; index avg `0.0512` n `23`; metal avg `0.0306` n `20`; unknown avg `0.4364` n `748`
- 24h: commodity avg `-0.26` n `12`; crypto_alt avg `1.4645` n `228`; crypto_major avg `1.1327` n `8`; equity avg `0.0203` n `87`; fx avg `-0.0359` n `6`; index avg `-0.2283` n `23`; metal avg `0.7289` n `20`; unknown avg `0.1247` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
