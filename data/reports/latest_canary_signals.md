# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T21:52:29.963294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1671` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.2016` n `228`; crypto_major avg `-0.1804` n `8`; equity avg `-0.0447` n `88`; fx avg `-0.0005` n `6`; index avg `-0.01` n `23`; metal avg `-0.0142` n `20`; unknown avg `0.0891` n `764`
- 1h: commodity avg `0.076` n `12`; crypto_alt avg `-0.3647` n `228`; crypto_major avg `-0.2947` n `8`; equity avg `-0.0022` n `88`; fx avg `0.0008` n `6`; index avg `-0.0139` n `23`; metal avg `-0.0106` n `20`; unknown avg `0.2211` n `764`
- 4h: commodity avg `0.1179` n `12`; crypto_alt avg `-1.0584` n `228`; crypto_major avg `-1.1705` n `8`; equity avg `-0.019` n `88`; fx avg `0.0001` n `6`; index avg `-0.0034` n `23`; metal avg `-0.0288` n `20`; unknown avg `0.0499` n `764`
- 24h: commodity avg `0.1663` n `12`; crypto_alt avg `-0.8403` n `228`; crypto_major avg `-0.8492` n `8`; equity avg `0.4642` n `88`; fx avg `-0.0064` n `6`; index avg `0.011` n `23`; metal avg `-0.0241` n `20`; unknown avg `-0.2474` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
