# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T11:22:34.440532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0319` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0474` n `13`; crypto_alt avg `0.0613` n `235`; crypto_major avg `-0.0364` n `8`; equity avg `0.0382` n `150`; fx avg `0.0031` n `6`; index avg `0.0161` n `26`; metal avg `0.04` n `20`; unknown avg `-0.0165` n `1077`
- 1h: commodity avg `0.0251` n `13`; crypto_alt avg `-0.8546` n `235`; crypto_major avg `-0.8819` n `8`; equity avg `-0.3249` n `150`; fx avg `0.0096` n `6`; index avg `-0.0271` n `26`; metal avg `-0.059` n `20`; unknown avg `2.2979` n `1075`
- 4h: commodity avg `0.2489` n `13`; crypto_alt avg `-0.6692` n `235`; crypto_major avg `-1.106` n `8`; equity avg `-0.5185` n `150`; fx avg `0.0396` n `6`; index avg `-0.0741` n `26`; metal avg `-0.145` n `20`; unknown avg `1.6872` n `1059`
- 24h: commodity avg `0.7079` n `13`; crypto_alt avg `0.1642` n `235`; crypto_major avg `-2.0236` n `8`; equity avg `-1.4633` n `150`; fx avg `0.0231` n `6`; index avg `-0.248` n `26`; metal avg `-0.1375` n `20`; unknown avg `416.7333` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
