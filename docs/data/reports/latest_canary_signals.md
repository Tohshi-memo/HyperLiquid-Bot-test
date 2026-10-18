# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T11:07:25.633300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0053` n `237`; crypto_major avg `-0.0177` n `8`; equity avg `0.0123` n `151`; fx avg `0.0005` n `6`; index avg `-0.0025` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.045` n `1191`
- 1h: commodity avg `-0.092` n `13`; crypto_alt avg `-0.2702` n `237`; crypto_major avg `-0.0535` n `8`; equity avg `0.0002` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0065` n `26`; metal avg `-0.002` n `20`; unknown avg `4.1251` n `1191`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `0.0057` n `237`; crypto_major avg `0.308` n `8`; equity avg `0.2221` n `151`; fx avg `0.0037` n `6`; index avg `0.0318` n `26`; metal avg `0.015` n `20`; unknown avg `4.9253` n `1079`
- 24h: commodity avg `0.0095` n `13`; crypto_alt avg `-2.3886` n `236`; crypto_major avg `-0.4705` n `8`; equity avg `-0.6783` n `151`; fx avg `-0.0557` n `6`; index avg `-0.0713` n `26`; metal avg `-0.0521` n `20`; unknown avg `4.623` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2031`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0746`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0629`, n `666`, weak_sample_signal
