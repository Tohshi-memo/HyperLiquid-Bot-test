# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T01:52:30.444707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0963` n `13`; crypto_alt avg `-0.2647` n `235`; crypto_major avg `-0.1644` n `8`; equity avg `-0.0195` n `150`; fx avg `0.0213` n `6`; index avg `0.011` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0907` n `1077`
- 1h: commodity avg `0.1099` n `13`; crypto_alt avg `-0.1659` n `235`; crypto_major avg `-0.1247` n `8`; equity avg `0.1183` n `150`; fx avg `0.0215` n `6`; index avg `0.0476` n `26`; metal avg `0.2926` n `20`; unknown avg `0.1108` n `1075`
- 4h: commodity avg `0.2263` n `13`; crypto_alt avg `1.1763` n `235`; crypto_major avg `0.5758` n `8`; equity avg `0.1223` n `150`; fx avg `-0.0416` n `6`; index avg `0.0143` n `26`; metal avg `0.323` n `20`; unknown avg `0.1716` n `1069`
- 24h: commodity avg `0.3877` n `13`; crypto_alt avg `-2.563` n `235`; crypto_major avg `-2.7258` n `8`; equity avg `-1.0163` n `150`; fx avg `-0.1801` n `6`; index avg `-0.1913` n `26`; metal avg `-0.2553` n `20`; unknown avg `247.8091` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
