# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T09:22:32.615963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.073` n `235`; crypto_major avg `0.0062` n `8`; equity avg `0.0872` n `151`; fx avg `0.0061` n `6`; index avg `0.0175` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.4933` n `1135`
- 1h: commodity avg `-0.0413` n `13`; crypto_alt avg `-0.7305` n `235`; crypto_major avg `-0.5262` n `8`; equity avg `-0.3451` n `151`; fx avg `-0.0097` n `6`; index avg `-0.014` n `26`; metal avg `-0.1099` n `20`; unknown avg `1.4331` n `1053`
- 4h: commodity avg `-0.0961` n `13`; crypto_alt avg `-0.6627` n `235`; crypto_major avg `-0.2448` n `8`; equity avg `-0.3584` n `151`; fx avg `-0.0224` n `6`; index avg `-0.0176` n `26`; metal avg `-0.1543` n `20`; unknown avg `1149.8572` n `1021`
- 24h: commodity avg `1.046` n `13`; crypto_alt avg `-0.806` n `235`; crypto_major avg `-0.2058` n `8`; equity avg `-0.5137` n `151`; fx avg `0.0396` n `6`; index avg `-0.0156` n `26`; metal avg `-0.4922` n `20`; unknown avg `1203.5463` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1325`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0736`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `666`, weak_sample_signal
