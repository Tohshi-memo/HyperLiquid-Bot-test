# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T20:37:28.208263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `13`; crypto_alt avg `-0.323` n `236`; crypto_major avg `-0.2196` n `8`; equity avg `-0.0534` n `151`; fx avg `-0.006` n `6`; index avg `-0.012` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0329` n `1114`
- 1h: commodity avg `0.1371` n `13`; crypto_alt avg `0.1232` n `236`; crypto_major avg `0.0143` n `8`; equity avg `-0.2443` n `151`; fx avg `0.0098` n `6`; index avg `-0.0373` n `26`; metal avg `0.0042` n `20`; unknown avg `31.5642` n `1086`
- 4h: commodity avg `0.1088` n `13`; crypto_alt avg `0.1249` n `236`; crypto_major avg `-0.009` n `8`; equity avg `-0.6159` n `151`; fx avg `0.0359` n `6`; index avg `-0.0917` n `26`; metal avg `-0.0171` n `20`; unknown avg `-0.0918` n `1086`
- 24h: commodity avg `-0.1266` n `13`; crypto_alt avg `-2.6702` n `236`; crypto_major avg `-2.0669` n `8`; equity avg `-4.2243` n `151`; fx avg `-0.1359` n `6`; index avg `-0.5755` n `26`; metal avg `-0.8278` n `20`; unknown avg `1305.5273` n `948`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.084`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0631`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0514`, n `666`, weak_sample_signal
