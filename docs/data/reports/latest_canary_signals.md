# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T20:52:32.353881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.1211` n `228`; crypto_major avg `-0.0117` n `8`; equity avg `-0.0009` n `88`; fx avg `0.0044` n `6`; index avg `0.002` n `23`; metal avg `0.0021` n `20`; unknown avg `0.0179` n `764`
- 1h: commodity avg `0.0347` n `12`; crypto_alt avg `0.1838` n `228`; crypto_major avg `0.0753` n `8`; equity avg `0.0966` n `88`; fx avg `-0.0002` n `6`; index avg `0.0344` n `23`; metal avg `0.015` n `20`; unknown avg `-0.0755` n `764`
- 4h: commodity avg `-0.0105` n `12`; crypto_alt avg `-1.3578` n `228`; crypto_major avg `-1.5248` n `8`; equity avg `-0.1191` n `88`; fx avg `0.002` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0621` n `20`; unknown avg `0.4403` n `764`
- 24h: commodity avg `0.0643` n `12`; crypto_alt avg `-0.3479` n `228`; crypto_major avg `-0.3184` n `8`; equity avg `0.5902` n `88`; fx avg `0.0821` n `6`; index avg `0.0533` n `23`; metal avg `-0.0285` n `20`; unknown avg `-0.3782` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
