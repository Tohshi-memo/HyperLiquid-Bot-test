# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T21:43:23.705292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0247` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1687` n `12`; crypto_alt avg `-0.4255` n `228`; crypto_major avg `-0.3511` n `8`; equity avg `0.027` n `88`; fx avg `0.0005` n `6`; index avg `0.001` n `23`; metal avg `0.0043` n `20`; unknown avg `-0.0134` n `764`
- 1h: commodity avg `0.0763` n `12`; crypto_alt avg `-0.2843` n `228`; crypto_major avg `-0.1261` n `8`; equity avg `0.0417` n `88`; fx avg `0.0057` n `6`; index avg `-0.0018` n `23`; metal avg `0.0057` n `20`; unknown avg `0.057` n `764`
- 4h: commodity avg `0.0689` n `12`; crypto_alt avg `-0.883` n `228`; crypto_major avg `-1.0171` n `8`; equity avg `0.0257` n `88`; fx avg `0.0035` n `6`; index avg `0.0076` n `23`; metal avg `-0.0148` n `20`; unknown avg `-0.0968` n `764`
- 24h: commodity avg `0.1239` n `12`; crypto_alt avg `-0.6383` n `228`; crypto_major avg `-0.6094` n `8`; equity avg `0.5706` n `88`; fx avg `-0.031` n `6`; index avg `0.0264` n `23`; metal avg `0.0123` n `20`; unknown avg `-0.1913` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
