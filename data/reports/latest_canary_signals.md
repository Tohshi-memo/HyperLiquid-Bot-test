# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T00:22:24.966235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2395` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0126` n `13`; crypto_alt avg `-0.2488` n `239`; crypto_major avg `-0.0402` n `8`; equity avg `-0.0108` n `162`; fx avg `-0.0018` n `6`; index avg `-0.1102` n `27`; metal avg `0.0043` n `20`; unknown avg `0.4217` n `1260`
- 1h: commodity avg `0.0345` n `13`; crypto_alt avg `0.4315` n `239`; crypto_major avg `0.6632` n `8`; equity avg `0.1057` n `162`; fx avg `-0.0184` n `6`; index avg `0.0001` n `27`; metal avg `0.0111` n `20`; unknown avg `0.508` n `1254`
- 4h: commodity avg `0.0564` n `13`; crypto_alt avg `-1.1995` n `239`; crypto_major avg `-1.306` n `8`; equity avg `-0.9349` n `162`; fx avg `-0.0286` n `6`; index avg `-0.0665` n `27`; metal avg `-0.0176` n `20`; unknown avg `4.1355` n `1166`
- 24h: commodity avg `-0.2253` n `13`; crypto_alt avg `-1.5346` n `239`; crypto_major avg `-2.9211` n `8`; equity avg `-4.1322` n `162`; fx avg `-0.0952` n `6`; index avg `-0.349` n `27`; metal avg `-0.3823` n `20`; unknown avg `60.1447` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
