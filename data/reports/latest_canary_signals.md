# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T07:37:39.377059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.0388` n `235`; crypto_major avg `0.0155` n `8`; equity avg `0.0795` n `151`; fx avg `0.0138` n `6`; index avg `0.0021` n `26`; metal avg `0.0194` n `20`; unknown avg `0.2187` n `1135`
- 1h: commodity avg `0.0361` n `13`; crypto_alt avg `0.0276` n `235`; crypto_major avg `0.0633` n `8`; equity avg `0.0294` n `151`; fx avg `-0.026` n `6`; index avg `0.029` n `26`; metal avg `-0.0801` n `20`; unknown avg `-0.1546` n `1133`
- 4h: commodity avg `-0.0312` n `13`; crypto_alt avg `-0.7881` n `235`; crypto_major avg `-0.4979` n `8`; equity avg `-0.6638` n `151`; fx avg `-0.0261` n `6`; index avg `-0.1001` n `26`; metal avg `-0.1514` n `20`; unknown avg `0.1442` n `1111`
- 24h: commodity avg `1.0628` n `13`; crypto_alt avg `-1.2215` n `235`; crypto_major avg `-0.7004` n `8`; equity avg `0.0603` n `151`; fx avg `-0.0029` n `6`; index avg `0.0232` n `26`; metal avg `-0.4963` n `20`; unknown avg `0.2782` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1552`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0786`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `666`, weak_sample_signal
