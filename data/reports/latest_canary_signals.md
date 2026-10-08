# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T14:07:32.160165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2765` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0758` n `13`; crypto_alt avg `0.5054` n `235`; crypto_major avg `0.2769` n `8`; equity avg `0.1418` n `150`; fx avg `0.0155` n `6`; index avg `0.0031` n `26`; metal avg `-0.0192` n `20`; unknown avg `0.2529` n `1051`
- 1h: commodity avg `0.0311` n `13`; crypto_alt avg `0.5941` n `235`; crypto_major avg `0.1186` n `8`; equity avg `-0.1763` n `150`; fx avg `0.0215` n `6`; index avg `0.008` n `26`; metal avg `-0.0125` n `20`; unknown avg `21.4338` n `1051`
- 4h: commodity avg `0.0862` n `13`; crypto_alt avg `-0.8464` n `235`; crypto_major avg `-1.2619` n `8`; equity avg `-0.3877` n `150`; fx avg `0.034` n `6`; index avg `0.0146` n `26`; metal avg `-0.1101` n `20`; unknown avg `2.9127` n `1045`
- 24h: commodity avg `0.7792` n `13`; crypto_alt avg `0.7828` n `235`; crypto_major avg `-1.828` n `8`; equity avg `-1.0951` n `150`; fx avg `0.0936` n `6`; index avg `-0.051` n `26`; metal avg `0.0747` n `20`; unknown avg `0.2244` n `968`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
