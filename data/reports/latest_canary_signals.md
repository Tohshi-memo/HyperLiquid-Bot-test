# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T17:22:34.976118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `0.3542` n `236`; crypto_major avg `0.2031` n `8`; equity avg `0.0032` n `151`; fx avg `-0.0069` n `6`; index avg `0.0034` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.7096` n `1193`
- 1h: commodity avg `-0.0161` n `13`; crypto_alt avg `-0.3211` n `236`; crypto_major avg `-0.1058` n `8`; equity avg `-0.0644` n `151`; fx avg `0.0037` n `6`; index avg `-0.017` n `26`; metal avg `-0.0183` n `20`; unknown avg `0.8817` n `1159`
- 4h: commodity avg `0.064` n `13`; crypto_alt avg `-0.5421` n `236`; crypto_major avg `-0.3721` n `8`; equity avg `-0.2412` n `151`; fx avg `-0.0326` n `6`; index avg `-0.0545` n `26`; metal avg `-0.0442` n `20`; unknown avg `2.5377` n `1135`
- 24h: commodity avg `0.1524` n `13`; crypto_alt avg `-1.0828` n `236`; crypto_major avg `0.0649` n `8`; equity avg `-0.7079` n `151`; fx avg `-0.0104` n `6`; index avg `-0.1081` n `26`; metal avg `-0.0283` n `20`; unknown avg `5.3656` n `1027`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1711`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1469`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
