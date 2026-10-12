# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T11:52:31.979432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.0655` n `235`; crypto_major avg `-0.0161` n `8`; equity avg `0.0169` n `151`; fx avg `-0.0106` n `6`; index avg `0.0042` n `26`; metal avg `-0.0046` n `20`; unknown avg `2.3021` n `1134`
- 1h: commodity avg `0.1274` n `13`; crypto_alt avg `-0.7093` n `235`; crypto_major avg `-0.4089` n `8`; equity avg `-0.2363` n `151`; fx avg `-0.0031` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0088` n `20`; unknown avg `1.7359` n `1115`
- 4h: commodity avg `0.3512` n `13`; crypto_alt avg `-1.4162` n `235`; crypto_major avg `-1.0053` n `8`; equity avg `-0.7512` n `151`; fx avg `-0.0186` n `6`; index avg `-0.1346` n `26`; metal avg `-0.0691` n `20`; unknown avg `0.3797` n `981`
- 24h: commodity avg `0.1538` n `13`; crypto_alt avg `1.2159` n `235`; crypto_major avg `0.73` n `8`; equity avg `-1.3249` n `151`; fx avg `-0.1357` n `6`; index avg `-0.1557` n `26`; metal avg `0.0322` n `20`; unknown avg `0.7152` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2443`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
