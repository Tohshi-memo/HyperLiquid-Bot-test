# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T08:22:29.282373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.1179` n `237`; crypto_major avg `0.1164` n `8`; equity avg `0.0738` n `151`; fx avg `-0.0026` n `6`; index avg `0.0058` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0311` n `1193`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.0657` n `237`; crypto_major avg `-0.0243` n `8`; equity avg `0.0998` n `151`; fx avg `0.0092` n `6`; index avg `0.0043` n `26`; metal avg `-0.0047` n `20`; unknown avg `-0.0409` n `1173`
- 4h: commodity avg `-0.0334` n `13`; crypto_alt avg `-0.7211` n `237`; crypto_major avg `-0.4198` n `8`; equity avg `0.1816` n `151`; fx avg `0.0041` n `6`; index avg `0.0372` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.099` n `1157`
- 24h: commodity avg `0.0779` n `13`; crypto_alt avg `-2.6897` n `236`; crypto_major avg `-0.9717` n `8`; equity avg `-0.7201` n `151`; fx avg `-0.0486` n `6`; index avg `-0.0816` n `26`; metal avg `-0.0626` n `20`; unknown avg `4.4079` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1722`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1325`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0814`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
