# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T11:37:26.527870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.0008` n `234`; crypto_major avg `0.0106` n `8`; equity avg `-0.0165` n `140`; fx avg `0.0011` n `6`; index avg `0.0045` n `26`; metal avg `-0.0312` n `20`; unknown avg `-0.2285` n `944`
- 1h: commodity avg `0.1125` n `12`; crypto_alt avg `0.1095` n `234`; crypto_major avg `0.2294` n `8`; equity avg `-0.112` n `140`; fx avg `-0.0033` n `6`; index avg `-0.0077` n `26`; metal avg `-0.1239` n `20`; unknown avg `0.3489` n `942`
- 4h: commodity avg `-0.4697` n `12`; crypto_alt avg `-0.0023` n `234`; crypto_major avg `0.6429` n `8`; equity avg `0.3673` n `140`; fx avg `-0.1268` n `6`; index avg `0.0574` n `26`; metal avg `0.0608` n `20`; unknown avg `1.5576` n `934`
- 24h: commodity avg `-0.5148` n `12`; crypto_alt avg `0.033` n `234`; crypto_major avg `1.284` n `8`; equity avg `1.0338` n `140`; fx avg `-0.2804` n `6`; index avg `0.2551` n `26`; metal avg `-0.2691` n `20`; unknown avg `1122.5208` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
