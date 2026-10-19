# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T11:37:34.538258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-0.1079` n `237`; crypto_major avg `-0.0816` n `8`; equity avg `-0.1385` n `151`; fx avg `-0.0133` n `6`; index avg `-0.0372` n `26`; metal avg `-0.0668` n `20`; unknown avg `-0.0163` n `1195`
- 1h: commodity avg `-0.018` n `13`; crypto_alt avg `-0.189` n `237`; crypto_major avg `-0.0232` n `8`; equity avg `-0.0015` n `151`; fx avg `-0.0022` n `6`; index avg `-0.0288` n `26`; metal avg `0.0323` n `20`; unknown avg `0.0073` n `1193`
- 4h: commodity avg `0.4195` n `13`; crypto_alt avg `-1.4514` n `237`; crypto_major avg `-1.0344` n `8`; equity avg `-0.3052` n `151`; fx avg `0.0148` n `6`; index avg `-0.0648` n `26`; metal avg `-0.0497` n `20`; unknown avg `1.1514` n `1149`
- 24h: commodity avg `-0.1301` n `13`; crypto_alt avg `-0.7732` n `237`; crypto_major avg `0.0309` n `8`; equity avg `2.3254` n `151`; fx avg `-0.0436` n `6`; index avg `0.403` n `26`; metal avg `0.2351` n `20`; unknown avg `0.8577` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1989`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1467`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1323`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0596`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
