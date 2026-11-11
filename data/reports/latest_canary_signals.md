# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T09:07:28.406784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `-0.2334` n `239`; crypto_major avg `-0.0442` n `8`; equity avg `0.0788` n `161`; fx avg `-0.0126` n `6`; index avg `0.0102` n `27`; metal avg `0.0267` n `20`; unknown avg `-0.0883` n `1253`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.2732` n `239`; crypto_major avg `-0.3171` n `8`; equity avg `0.1668` n `161`; fx avg `-0.0594` n `6`; index avg `0.0146` n `27`; metal avg `0.0469` n `20`; unknown avg `0.169` n `1251`
- 4h: commodity avg `0.0353` n `13`; crypto_alt avg `-0.6886` n `239`; crypto_major avg `-0.0945` n `8`; equity avg `0.7017` n `161`; fx avg `-0.0665` n `6`; index avg `0.0252` n `27`; metal avg `0.1092` n `20`; unknown avg `0.1345` n `1197`
- 24h: commodity avg `0.5404` n `13`; crypto_alt avg `-1.1279` n `239`; crypto_major avg `-1.8592` n `8`; equity avg `2.1545` n `161`; fx avg `-0.262` n `6`; index avg `0.2468` n `27`; metal avg `0.1151` n `20`; unknown avg `49.9385` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
