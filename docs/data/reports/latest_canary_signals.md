# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T07:37:25.889968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `13`; crypto_alt avg `0.2908` n `239`; crypto_major avg `0.199` n `8`; equity avg `0.0577` n `162`; fx avg `0.0031` n `6`; index avg `0.0041` n `27`; metal avg `0.0017` n `20`; unknown avg `0.2476` n `1262`
- 1h: commodity avg `0.026` n `13`; crypto_alt avg `-0.6803` n `239`; crypto_major avg `-0.3259` n `8`; equity avg `-0.041` n `162`; fx avg `-0.0058` n `6`; index avg `-0.0028` n `27`; metal avg `0.0066` n `20`; unknown avg `11.1749` n `1256`
- 4h: commodity avg `0.0289` n `13`; crypto_alt avg `-0.594` n `239`; crypto_major avg `0.1911` n `8`; equity avg `0.0683` n `162`; fx avg `-0.0002` n `6`; index avg `0.0083` n `27`; metal avg `0.0075` n `20`; unknown avg `5.1676` n `1214`
- 24h: commodity avg `-0.1002` n `13`; crypto_alt avg `-3.0818` n `239`; crypto_major avg `-3.0561` n `8`; equity avg `-2.6742` n `162`; fx avg `-0.1368` n `6`; index avg `-0.2138` n `27`; metal avg `-0.3796` n `20`; unknown avg `64.625` n `1018`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
