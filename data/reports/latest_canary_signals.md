# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T00:37:31.251421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `13`; crypto_alt avg `-0.1429` n `236`; crypto_major avg `-0.1332` n `8`; equity avg `0.144` n `151`; fx avg `0.0091` n `6`; index avg `0.0032` n `26`; metal avg `0.0036` n `20`; unknown avg `0.1333` n `1136`
- 1h: commodity avg `-0.0457` n `13`; crypto_alt avg `-0.0911` n `236`; crypto_major avg `0.0757` n `8`; equity avg `0.2392` n `151`; fx avg `0.0892` n `6`; index avg `-0.0816` n `26`; metal avg `0.196` n `20`; unknown avg `0.3321` n `1128`
- 4h: commodity avg `-0.1357` n `13`; crypto_alt avg `0.1941` n `236`; crypto_major avg `0.0314` n `8`; equity avg `-1.1711` n `151`; fx avg `0.1378` n `6`; index avg `-0.2744` n `26`; metal avg `0.1959` n `20`; unknown avg `0.3581` n `1040`
- 24h: commodity avg `-0.3071` n `13`; crypto_alt avg `-2.9088` n `236`; crypto_major avg `-2.4271` n `8`; equity avg `-5.6668` n `151`; fx avg `-0.0163` n `6`; index avg `-0.8949` n `26`; metal avg `-0.6211` n `20`; unknown avg `1391.9122` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
