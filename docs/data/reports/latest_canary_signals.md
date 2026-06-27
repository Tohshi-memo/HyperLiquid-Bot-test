# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T20:37:30.716543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3986` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0192` n `228`; crypto_major avg `-0.0223` n `8`; equity avg `0.0302` n `88`; fx avg `-0.0086` n `6`; index avg `0.0059` n `23`; metal avg `0.0009` n `20`; unknown avg `-0.0987` n `764`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `0.5655` n `228`; crypto_major avg `0.2631` n `8`; equity avg `0.0792` n `88`; fx avg `-0.0036` n `6`; index avg `0.031` n `23`; metal avg `0.0129` n `20`; unknown avg `-0.0782` n `764`
- 4h: commodity avg `-0.0129` n `12`; crypto_alt avg `-1.2204` n `228`; crypto_major avg `-1.4029` n `8`; equity avg `-0.1057` n `88`; fx avg `-0.0045` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0566` n `20`; unknown avg `0.2732` n `764`
- 24h: commodity avg `0.1171` n `12`; crypto_alt avg `-0.2379` n `228`; crypto_major avg `-0.3899` n `8`; equity avg `0.5979` n `88`; fx avg `0.0796` n `6`; index avg `0.0347` n `23`; metal avg `0.1468` n `20`; unknown avg `-0.4394` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
