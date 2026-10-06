# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T09:37:34.245870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0769` n `13`; crypto_alt avg `-0.1889` n `235`; crypto_major avg `-0.3374` n `8`; equity avg `0.0448` n `149`; fx avg `0.0138` n `6`; index avg `0.0095` n `26`; metal avg `0.0231` n `20`; unknown avg `0.5022` n `1075`
- 1h: commodity avg `-0.1476` n `13`; crypto_alt avg `-0.2581` n `235`; crypto_major avg `-0.1271` n `8`; equity avg `0.1212` n `149`; fx avg `0.018` n `6`; index avg `0.0122` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.6599` n `1072`
- 4h: commodity avg `-0.4949` n `13`; crypto_alt avg `0.0021` n `235`; crypto_major avg `-0.1273` n `8`; equity avg `0.1924` n `149`; fx avg `0.0352` n `6`; index avg `0.051` n `26`; metal avg `0.1473` n `20`; unknown avg `-0.1615` n `976`
- 24h: commodity avg `-0.6398` n `13`; crypto_alt avg `-0.8811` n `235`; crypto_major avg `-0.5194` n `8`; equity avg `0.5324` n `149`; fx avg `0.0207` n `6`; index avg `0.227` n `26`; metal avg `-0.1012` n `20`; unknown avg `-0.1131` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
