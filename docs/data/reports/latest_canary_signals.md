# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T02:37:28.683915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `0.0073` n `239`; crypto_major avg `-0.1358` n `8`; equity avg `0.0611` n `162`; fx avg `-0.0053` n `6`; index avg `0.015` n `27`; metal avg `0.0317` n `20`; unknown avg `2.5872` n `1266`
- 1h: commodity avg `-0.0432` n `13`; crypto_alt avg `0.1536` n `239`; crypto_major avg `-0.1341` n `8`; equity avg `-0.0796` n `162`; fx avg `-0.0001` n `6`; index avg `-0.0103` n `27`; metal avg `0.0964` n `20`; unknown avg `1.693` n `1264`
- 4h: commodity avg `-0.1671` n `13`; crypto_alt avg `-0.4923` n `239`; crypto_major avg `-0.8033` n `8`; equity avg `-0.0084` n `162`; fx avg `0.0378` n `6`; index avg `0.0058` n `27`; metal avg `0.1783` n `20`; unknown avg `2.0409` n `1226`
- 24h: commodity avg `-1.0305` n `13`; crypto_alt avg `-0.8722` n `239`; crypto_major avg `-0.4772` n `8`; equity avg `-3.5011` n `162`; fx avg `-0.0521` n `6`; index avg `-0.3396` n `27`; metal avg `-0.1623` n `20`; unknown avg `546.7197` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
