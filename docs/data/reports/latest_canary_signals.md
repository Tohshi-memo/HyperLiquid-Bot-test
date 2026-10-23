# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T18:37:29.524446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `13`; crypto_alt avg `-0.1905` n `237`; crypto_major avg `-0.1041` n `8`; equity avg `-0.0542` n `152`; fx avg `0.001` n `6`; index avg `-0.0139` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.034` n `1230`
- 1h: commodity avg `-0.0708` n `13`; crypto_alt avg `0.0875` n `237`; crypto_major avg `-0.1262` n `8`; equity avg `0.0206` n `152`; fx avg `0.0108` n `6`; index avg `0.0168` n `26`; metal avg `0.0518` n `20`; unknown avg `-0.1242` n `1229`
- 4h: commodity avg `-0.0162` n `13`; crypto_alt avg `0.156` n `237`; crypto_major avg `-0.2117` n `8`; equity avg `0.0212` n `152`; fx avg `-0.0251` n `6`; index avg `0.0471` n `26`; metal avg `0.0763` n `20`; unknown avg `-0.8236` n `1197`
- 24h: commodity avg `0.3142` n `13`; crypto_alt avg `1.2725` n `237`; crypto_major avg `0.838` n `8`; equity avg `1.4842` n `152`; fx avg `-0.1094` n `6`; index avg `0.0696` n `26`; metal avg `-0.1587` n `20`; unknown avg `-0.462` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
