# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T08:37:39.231661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `13`; crypto_alt avg `-0.2996` n `235`; crypto_major avg `-0.2335` n `8`; equity avg `-0.1885` n `151`; fx avg `-0.0143` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0526` n `20`; unknown avg `0.2353` n `1135`
- 1h: commodity avg `-0.0726` n `13`; crypto_alt avg `0.0292` n `235`; crypto_major avg `0.0826` n `8`; equity avg `0.0747` n `151`; fx avg `-0.0062` n `6`; index avg `0.0309` n `26`; metal avg `0.031` n `20`; unknown avg `1126.6075` n `1117`
- 4h: commodity avg `-0.0693` n `13`; crypto_alt avg `-0.788` n `235`; crypto_major avg `-0.3609` n `8`; equity avg `-0.5014` n `151`; fx avg `-0.0389` n `6`; index avg `-0.0725` n `26`; metal avg `-0.1241` n `20`; unknown avg `1142.9803` n `1101`
- 24h: commodity avg `1.0878` n `13`; crypto_alt avg `-0.9215` n `235`; crypto_major avg `-0.4932` n `8`; equity avg `-0.4239` n `151`; fx avg `0.0158` n `6`; index avg `-0.0185` n `26`; metal avg `-0.473` n `20`; unknown avg `1285.03` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1529`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.133`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0712`, n `666`, weak_sample_signal
