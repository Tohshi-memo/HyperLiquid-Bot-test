# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T18:37:33.919337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1921` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0283` n `12`; crypto_alt avg `0.0839` n `234`; crypto_major avg `0.1245` n `8`; equity avg `-0.0239` n `142`; fx avg `0.0079` n `6`; index avg `-0.006` n `26`; metal avg `0.0359` n `20`; unknown avg `10.1224` n `962`
- 1h: commodity avg `-0.2337` n `12`; crypto_alt avg `0.7172` n `234`; crypto_major avg `0.5629` n `8`; equity avg `0.0437` n `142`; fx avg `0.0207` n `6`; index avg `0.0428` n `26`; metal avg `0.2057` n `20`; unknown avg `7.0431` n `960`
- 4h: commodity avg `-0.3088` n `12`; crypto_alt avg `-1.6647` n `234`; crypto_major avg `-1.2501` n `8`; equity avg `-0.7065` n `142`; fx avg `-0.0266` n `6`; index avg `-0.058` n `26`; metal avg `0.1113` n `20`; unknown avg `6.0116` n `920`
- 24h: commodity avg `-0.6647` n `12`; crypto_alt avg `0.1691` n `234`; crypto_major avg `-0.8589` n `8`; equity avg `0.3108` n `142`; fx avg `-0.1629` n `6`; index avg `-0.009` n `26`; metal avg `0.0239` n `20`; unknown avg `2.5236` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
