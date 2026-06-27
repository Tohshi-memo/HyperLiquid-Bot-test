# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T00:37:26.342611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.2433` n `228`; crypto_major avg `-0.3358` n `8`; equity avg `-0.0631` n `88`; fx avg `-0.0114` n `6`; index avg `-0.0028` n `23`; metal avg `-0.0117` n `20`; unknown avg `0.5221` n `764`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.2304` n `228`; crypto_major avg `-0.544` n `8`; equity avg `-0.0719` n `88`; fx avg `0.0016` n `6`; index avg `0.0039` n `23`; metal avg `0.0014` n `20`; unknown avg `0.3673` n `764`
- 4h: commodity avg `0.0893` n `12`; crypto_alt avg `-0.0952` n `228`; crypto_major avg `-0.1518` n `8`; equity avg `0.2437` n `88`; fx avg `0.053` n `6`; index avg `0.0355` n `23`; metal avg `0.2078` n `20`; unknown avg `0.3086` n `748`
- 24h: commodity avg `-0.2553` n `12`; crypto_alt avg `1.1813` n `228`; crypto_major avg `0.8553` n `8`; equity avg `0.1625` n `87`; fx avg `-0.0491` n `6`; index avg `-0.2014` n `23`; metal avg `0.8315` n `20`; unknown avg `0.2808` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
