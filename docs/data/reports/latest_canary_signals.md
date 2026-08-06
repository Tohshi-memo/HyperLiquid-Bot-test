# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T09:07:28.821579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0824` n `12`; crypto_alt avg `0.0153` n `230`; crypto_major avg `-0.1721` n `8`; equity avg `-0.1625` n `108`; fx avg `-0.0021` n `6`; index avg `-0.0447` n `25`; metal avg `0.0223` n `20`; unknown avg `0.0136` n `782`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.1031` n `230`; crypto_major avg `0.0754` n `8`; equity avg `-0.0076` n `108`; fx avg `-0.0366` n `6`; index avg `-0.0218` n `25`; metal avg `0.1477` n `20`; unknown avg `0.0009` n `782`
- 4h: commodity avg `0.124` n `12`; crypto_alt avg `0.11` n `230`; crypto_major avg `-0.2581` n `8`; equity avg `-0.5287` n `108`; fx avg `0.0654` n `6`; index avg `-0.1239` n `25`; metal avg `0.1235` n `20`; unknown avg `0.0741` n `750`
- 24h: commodity avg `-0.1669` n `12`; crypto_alt avg `0.3681` n `230`; crypto_major avg `-0.2383` n `8`; equity avg `-1.603` n `108`; fx avg `0.0025` n `6`; index avg `-0.3359` n `25`; metal avg `0.45` n `20`; unknown avg `0.9117` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
