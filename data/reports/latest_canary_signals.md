# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T13:07:29.077762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2729` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.038` n `13`; crypto_alt avg `0.1809` n `235`; crypto_major avg `0.1293` n `8`; equity avg `0.1577` n `150`; fx avg `0.002` n `6`; index avg `0.0423` n `26`; metal avg `0.0651` n `20`; unknown avg `0.2508` n `1075`
- 1h: commodity avg `-0.0383` n `13`; crypto_alt avg `-0.2084` n `235`; crypto_major avg `-0.117` n `8`; equity avg `0.0872` n `150`; fx avg `-0.0054` n `6`; index avg `0.0191` n `26`; metal avg `-0.044` n `20`; unknown avg `-0.2604` n `1075`
- 4h: commodity avg `0.1016` n `13`; crypto_alt avg `-1.0741` n `235`; crypto_major avg `-1.2725` n `8`; equity avg `-0.2584` n `150`; fx avg `0.0151` n `6`; index avg `0.0004` n `26`; metal avg `-0.1524` n `20`; unknown avg `0.6327` n `1069`
- 24h: commodity avg `0.7432` n `13`; crypto_alt avg `-0.0197` n `235`; crypto_major avg `-2.1396` n `8`; equity avg `-1.1366` n `150`; fx avg `0.0588` n `6`; index avg `-0.1448` n `26`; metal avg `0.0686` n `20`; unknown avg `416.8095` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
