# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T15:07:29.918955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `-0.2191` n `235`; crypto_major avg `-0.1228` n `8`; equity avg `0.0044` n `143`; fx avg `-0.0019` n `6`; index avg `0.0017` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0618` n `1020`
- 1h: commodity avg `0.0703` n `13`; crypto_alt avg `0.4031` n `235`; crypto_major avg `0.2424` n `8`; equity avg `0.0169` n `143`; fx avg `-0.0086` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.033` n `972`
- 4h: commodity avg `0.1147` n `13`; crypto_alt avg `0.5441` n `235`; crypto_major avg `0.3636` n `8`; equity avg `-0.0007` n `143`; fx avg `-0.0186` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.2007` n `946`
- 24h: commodity avg `0.7193` n `13`; crypto_alt avg `-0.8431` n `235`; crypto_major avg `-0.6742` n `8`; equity avg `-0.1935` n `143`; fx avg `-0.0534` n `6`; index avg `-0.0043` n `26`; metal avg `-0.002` n `20`; unknown avg `0.6905` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
