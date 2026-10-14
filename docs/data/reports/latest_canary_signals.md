# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T10:34:24.814568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `0.1081` n `235`; crypto_major avg `0.1124` n `8`; equity avg `-0.0461` n `151`; fx avg `-0.0146` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0265` n `20`; unknown avg `-0.0006` n `1135`
- 1h: commodity avg `0.0684` n `13`; crypto_alt avg `0.1079` n `235`; crypto_major avg `0.1739` n `8`; equity avg `0.0321` n `151`; fx avg `-0.0145` n `6`; index avg `-0.0059` n `26`; metal avg `0.0407` n `20`; unknown avg `0.1663` n `1133`
- 4h: commodity avg `0.0941` n `13`; crypto_alt avg `-0.6483` n `235`; crypto_major avg `-0.1794` n `8`; equity avg `-0.1638` n `151`; fx avg `-0.0437` n `6`; index avg `0.0389` n `26`; metal avg `-0.0911` n `20`; unknown avg `1192.4543` n `1037`
- 24h: commodity avg `1.2816` n `13`; crypto_alt avg `-0.1952` n `235`; crypto_major avg `0.2563` n `8`; equity avg `-0.3518` n `151`; fx avg `0.0074` n `6`; index avg `0.0059` n `26`; metal avg `-0.4633` n `20`; unknown avg `1268.0786` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1515`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1306`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0743`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0715`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
