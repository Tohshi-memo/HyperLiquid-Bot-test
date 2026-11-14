# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T19:37:24.521537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3427` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0026` n `13`; crypto_alt avg `-0.1629` n `239`; crypto_major avg `-0.1278` n `8`; equity avg `-0.0316` n `162`; fx avg `0.0046` n `6`; index avg `-0.0008` n `27`; metal avg `0.0008` n `20`; unknown avg `0.2142` n `1262`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `-0.7066` n `239`; crypto_major avg `-0.6097` n `8`; equity avg `-0.1627` n `162`; fx avg `0.0028` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0245` n `20`; unknown avg `8.2809` n `1260`
- 4h: commodity avg `-0.0397` n `13`; crypto_alt avg `-1.7613` n `239`; crypto_major avg `-1.379` n `8`; equity avg `-0.336` n `162`; fx avg `0.0219` n `6`; index avg `-0.0363` n `27`; metal avg `-0.0905` n `20`; unknown avg `6.2222` n `1254`
- 24h: commodity avg `-0.0129` n `13`; crypto_alt avg `-7.4817` n `239`; crypto_major avg `-6.9766` n `8`; equity avg `-2.0091` n `162`; fx avg `-0.0077` n `6`; index avg `-0.1708` n `27`; metal avg `-0.2574` n `20`; unknown avg `1.6417` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
