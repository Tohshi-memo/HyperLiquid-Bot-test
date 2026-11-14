# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T22:37:37.628688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.4442` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.3404` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.0675` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.7077` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.1123` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.7306` n `239`; crypto_major avg `-0.9897` n `8`; equity avg `-0.1442` n `162`; fx avg `0.0017` n `6`; index avg `-0.0112` n `27`; metal avg `-0.015` n `20`; unknown avg `-0.2045` n `1262`
- 1h: commodity avg `0.0665` n `13`; crypto_alt avg `-0.5582` n `239`; crypto_major avg `-1.1002` n `8`; equity avg `-0.0352` n `162`; fx avg `0.0067` n `6`; index avg `0.0121` n `27`; metal avg `0.0533` n `20`; unknown avg `0.2126` n `1254`
- 4h: commodity avg `0.0821` n `13`; crypto_alt avg `-4.0771` n `239`; crypto_major avg `-4.3621` n `8`; equity avg `-0.6544` n `162`; fx avg `0.006` n `6`; index avg `-0.0217` n `27`; metal avg `-0.2946` n `20`; unknown avg `0.1421` n `1208`
- 24h: commodity avg `0.0263` n `13`; crypto_alt avg `-9.407` n `239`; crypto_major avg `-9.2362` n `8`; equity avg `-1.7925` n `162`; fx avg `-0.0035` n `6`; index avg `-0.1407` n `27`; metal avg `-0.5127` n `20`; unknown avg `0.1533` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
