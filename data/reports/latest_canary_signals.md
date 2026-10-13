# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T20:52:45.014093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `-0.0326` n `235`; crypto_major avg `-0.0017` n `8`; equity avg `0.0366` n `151`; fx avg `-0.0062` n `6`; index avg `0.0103` n `26`; metal avg `0.0127` n `20`; unknown avg `6.19` n `1135`
- 1h: commodity avg `0.0733` n `13`; crypto_alt avg `0.1762` n `235`; crypto_major avg `0.1057` n `8`; equity avg `0.2661` n `151`; fx avg `-0.0114` n `6`; index avg `0.0207` n `26`; metal avg `-0.0322` n `20`; unknown avg `0.6663` n `1081`
- 4h: commodity avg `0.24` n `13`; crypto_alt avg `0.1858` n `235`; crypto_major avg `-0.1143` n `8`; equity avg `0.2105` n `151`; fx avg `0.0158` n `6`; index avg `0.0235` n `26`; metal avg `0.0072` n `20`; unknown avg `1.7787` n `1081`
- 24h: commodity avg `0.9376` n `13`; crypto_alt avg `-1.5106` n `235`; crypto_major avg `-0.713` n `8`; equity avg `-0.6989` n `151`; fx avg `0.1676` n `6`; index avg `-0.1505` n `26`; metal avg `-0.2816` n `20`; unknown avg `1.9847` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1573`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0918`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `666`, weak_sample_signal
