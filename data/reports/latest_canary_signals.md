# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T15:22:37.093087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6273` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0841` n `13`; crypto_alt avg `0.1713` n `235`; crypto_major avg `0.3391` n `8`; equity avg `-0.0223` n `151`; fx avg `-0.0054` n `6`; index avg `0.0134` n `26`; metal avg `0.022` n `20`; unknown avg `0.1368` n `1137`
- 1h: commodity avg `-0.0296` n `13`; crypto_alt avg `-0.0332` n `235`; crypto_major avg `0.1276` n `8`; equity avg `-0.4387` n `151`; fx avg `-0.0123` n `6`; index avg `-0.0518` n `26`; metal avg `-0.0853` n `20`; unknown avg `-0.0266` n `1134`
- 4h: commodity avg `-0.2663` n `13`; crypto_alt avg `-2.2715` n `235`; crypto_major avg `-1.9238` n `8`; equity avg `-2.2502` n `151`; fx avg `-0.1301` n `6`; index avg `-0.2965` n `26`; metal avg `-0.6479` n `20`; unknown avg `3.2237` n `1102`
- 24h: commodity avg `0.0696` n `13`; crypto_alt avg `-2.8425` n `235`; crypto_major avg `-2.1752` n `8`; equity avg `-2.3718` n `151`; fx avg `-0.1689` n `6`; index avg `-0.2673` n `26`; metal avg `-0.8069` n `20`; unknown avg `1263.0509` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.083`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0793`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
