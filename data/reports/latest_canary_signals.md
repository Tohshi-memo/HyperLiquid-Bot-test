# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T18:07:45.992007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `0.1267` n `235`; crypto_major avg `0.0644` n `8`; equity avg `-0.0052` n `144`; fx avg `0.0101` n `6`; index avg `-0.0002` n `26`; metal avg `0.0417` n `20`; unknown avg `0.2188` n `1077`
- 1h: commodity avg `-0.0031` n `13`; crypto_alt avg `0.509` n `235`; crypto_major avg `0.2914` n `8`; equity avg `0.2539` n `144`; fx avg `0.0213` n `6`; index avg `0.0272` n `26`; metal avg `0.0821` n `20`; unknown avg `40.0964` n `1077`
- 4h: commodity avg `-0.0446` n `13`; crypto_alt avg `-0.8087` n `235`; crypto_major avg `-0.8062` n `8`; equity avg `0.4117` n `144`; fx avg `0.0305` n `6`; index avg `0.1156` n `26`; metal avg `0.0156` n `20`; unknown avg `1.3243` n `1001`
- 24h: commodity avg `-0.3054` n `13`; crypto_alt avg `0.1808` n `235`; crypto_major avg `0.2179` n `8`; equity avg `0.3587` n `144`; fx avg `-0.0832` n `6`; index avg `0.116` n `26`; metal avg `0.1915` n `20`; unknown avg `-0.2102` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
