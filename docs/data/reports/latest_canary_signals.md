# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T06:22:34.434782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0128` n `234`; crypto_major avg `-0.0446` n `8`; equity avg `-0.1272` n `140`; fx avg `-0.0081` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0202` n `20`; unknown avg `0.1519` n `940`
- 1h: commodity avg `0.0552` n `12`; crypto_alt avg `0.3517` n `234`; crypto_major avg `0.2259` n `8`; equity avg `-0.1628` n `140`; fx avg `0.0151` n `6`; index avg `-0.0112` n `26`; metal avg `-0.1434` n `20`; unknown avg `8.3485` n `914`
- 4h: commodity avg `0.1916` n `12`; crypto_alt avg `-0.1685` n `234`; crypto_major avg `-0.1893` n `8`; equity avg `-0.9397` n `140`; fx avg `-0.0145` n `6`; index avg `-0.1162` n `26`; metal avg `-0.2287` n `20`; unknown avg `1.7721` n `908`
- 24h: commodity avg `-0.0424` n `12`; crypto_alt avg `2.2696` n `234`; crypto_major avg `3.4882` n `8`; equity avg `1.3408` n `140`; fx avg `-0.2296` n `6`; index avg `0.3348` n `26`; metal avg `-0.1723` n `20`; unknown avg `6.6906` n `770`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
