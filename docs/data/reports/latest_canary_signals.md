# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T18:07:31.327770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `0.0171` n `237`; crypto_major avg `0.0784` n `8`; equity avg `0.0049` n `151`; fx avg `0.0083` n `6`; index avg `0.0003` n `26`; metal avg `0.0106` n `20`; unknown avg `12.6689` n `1192`
- 1h: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.3464` n `237`; crypto_major avg `0.006` n `8`; equity avg `-0.1163` n `151`; fx avg `0.0119` n `6`; index avg `-0.0208` n `26`; metal avg `0.006` n `20`; unknown avg `0.2535` n `1190`
- 4h: commodity avg `-0.023` n `13`; crypto_alt avg `-0.5184` n `237`; crypto_major avg `-0.2815` n `8`; equity avg `-0.2477` n `151`; fx avg `0.008` n `6`; index avg `-0.0432` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.6707` n `1159`
- 24h: commodity avg `-0.0122` n `13`; crypto_alt avg `-3.194` n `236`; crypto_major avg `-1.2172` n `8`; equity avg `-1.0066` n `151`; fx avg `0.0077` n `6`; index avg `-0.1099` n `26`; metal avg `-0.0315` n `20`; unknown avg `0.5201` n `1015`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
