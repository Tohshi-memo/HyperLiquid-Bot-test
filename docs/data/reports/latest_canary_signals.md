# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T13:37:29.658237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `0.0695` n `237`; crypto_major avg `0.1658` n `8`; equity avg `0.4467` n `151`; fx avg `0.0116` n `6`; index avg `0.0826` n `26`; metal avg `-0.0906` n `20`; unknown avg `4.0169` n `1201`
- 1h: commodity avg `0.1801` n `13`; crypto_alt avg `-0.2407` n `237`; crypto_major avg `0.0688` n `8`; equity avg `0.1144` n `151`; fx avg `0.0491` n `6`; index avg `0.0529` n `26`; metal avg `-0.1048` n `20`; unknown avg `83.3549` n `1199`
- 4h: commodity avg `0.1632` n `13`; crypto_alt avg `-0.0358` n `237`; crypto_major avg `0.2511` n `8`; equity avg `0.4404` n `151`; fx avg `0.0221` n `6`; index avg `0.1323` n `26`; metal avg `-0.0945` n `20`; unknown avg `23.9717` n `1193`
- 24h: commodity avg `-0.1527` n `13`; crypto_alt avg `-2.5239` n `237`; crypto_major avg `-1.7886` n `8`; equity avg `-1.8059` n `151`; fx avg `-0.1115` n `6`; index avg `-0.2274` n `26`; metal avg `-0.6371` n `20`; unknown avg `17.9227` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
