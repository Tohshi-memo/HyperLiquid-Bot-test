# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T08:52:27.028706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `13`; crypto_alt avg `-0.157` n `235`; crypto_major avg `-0.1933` n `8`; equity avg `-0.176` n `151`; fx avg `-0.0051` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0491` n `20`; unknown avg `0.7334` n `1087`
- 1h: commodity avg `0.0436` n `13`; crypto_alt avg `-0.1171` n `235`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0471` n `151`; fx avg `0.0026` n `6`; index avg `0.0147` n `26`; metal avg `-0.0284` n `20`; unknown avg `1097.9891` n `1069`
- 4h: commodity avg `-0.0427` n `13`; crypto_alt avg `-0.9559` n `235`; crypto_major avg `-0.4976` n `8`; equity avg `-0.6989` n `151`; fx avg `-0.0338` n `6`; index avg `-0.0934` n `26`; metal avg `-0.1979` n `20`; unknown avg `1114.6709` n `1053`
- 24h: commodity avg `1.0846` n `13`; crypto_alt avg `-0.9171` n `235`; crypto_major avg `-0.4221` n `8`; equity avg `-0.535` n `151`; fx avg `0.0351` n `6`; index avg `-0.0145` n `26`; metal avg `-0.4846` n `20`; unknown avg `1198.332` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1326`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0714`, n `666`, weak_sample_signal
