# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T12:37:29.083416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3323` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `0.0037` n `239`; crypto_major avg `0.1406` n `8`; equity avg `-0.006` n `165`; fx avg `0.0312` n `6`; index avg `-0.0154` n `27`; metal avg `0.001` n `20`; unknown avg `158.9503` n `1262`
- 1h: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.5603` n `239`; crypto_major avg `-0.6342` n `8`; equity avg `-0.4985` n `165`; fx avg `0.0355` n `6`; index avg `-0.0421` n `27`; metal avg `-0.0697` n `20`; unknown avg `-0.0394` n `1254`
- 4h: commodity avg `0.1655` n `13`; crypto_alt avg `-1.4209` n `239`; crypto_major avg `-1.5075` n `8`; equity avg `-1.5511` n `165`; fx avg `0.0522` n `6`; index avg `-0.1752` n `27`; metal avg `-0.1314` n `20`; unknown avg `27.193` n `1240`
- 24h: commodity avg `-0.3887` n `13`; crypto_alt avg `-3.8862` n `239`; crypto_major avg `-3.7447` n `8`; equity avg `-8.4215` n `165`; fx avg `-0.0161` n `6`; index avg `-0.8463` n `27`; metal avg `-1.2366` n `20`; unknown avg `33.6484` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
