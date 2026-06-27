# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T01:07:31.793362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0263` n `228`; crypto_major avg `-0.1089` n `8`; equity avg `-0.0033` n `88`; fx avg `0.0165` n `6`; index avg `0.0094` n `23`; metal avg `0.0017` n `20`; unknown avg `-0.2033` n `764`
- 1h: commodity avg `-0.0423` n `12`; crypto_alt avg `-0.2125` n `228`; crypto_major avg `-0.513` n `8`; equity avg `-0.1494` n `88`; fx avg `0.0188` n `6`; index avg `0.0055` n `23`; metal avg `-0.0276` n `20`; unknown avg `0.1974` n `764`
- 4h: commodity avg `0.0543` n `12`; crypto_alt avg `0.3321` n `228`; crypto_major avg `0.237` n `8`; equity avg `0.2411` n `88`; fx avg `0.0367` n `6`; index avg `0.0506` n `23`; metal avg `0.0645` n `20`; unknown avg `0.0285` n `748`
- 24h: commodity avg `-0.2083` n `12`; crypto_alt avg `1.7452` n `228`; crypto_major avg `1.5269` n `8`; equity avg `0.4094` n `87`; fx avg `-0.0358` n `6`; index avg `-0.1615` n `23`; metal avg `0.8768` n `20`; unknown avg `0.2581` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
