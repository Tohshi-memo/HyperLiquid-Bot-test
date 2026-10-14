# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T21:22:25.261776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `13`; crypto_alt avg `0.0096` n `236`; crypto_major avg `0.0429` n `8`; equity avg `-0.0565` n `151`; fx avg `0.0022` n `6`; index avg `0.0346` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.0593` n `1134`
- 1h: commodity avg `0.0133` n `13`; crypto_alt avg `-0.3454` n `236`; crypto_major avg `-0.4074` n `8`; equity avg `-0.2872` n `151`; fx avg `-0.0181` n `6`; index avg `-0.0036` n `26`; metal avg `0.0043` n `20`; unknown avg `3.2423` n `1104`
- 4h: commodity avg `0.05` n `13`; crypto_alt avg `-0.2391` n `236`; crypto_major avg `-0.3277` n `8`; equity avg `-0.8322` n `151`; fx avg `-0.0048` n `6`; index avg `-0.0784` n `26`; metal avg `-0.011` n `20`; unknown avg `0.4934` n `1078`
- 24h: commodity avg `-0.1176` n `13`; crypto_alt avg `-2.4812` n `236`; crypto_major avg `-2.1762` n `8`; equity avg `-4.456` n `151`; fx avg `-0.134` n `6`; index avg `-0.5867` n `26`; metal avg `-0.8513` n `20`; unknown avg `1309.1647` n `946`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0679`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0525`, n `666`, weak_sample_signal
