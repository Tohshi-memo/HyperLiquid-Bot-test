# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T22:37:35.177185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `13`; crypto_alt avg `-0.0369` n `239`; crypto_major avg `-0.0964` n `8`; equity avg `0.0337` n `162`; fx avg `0.0056` n `6`; index avg `0.0072` n `27`; metal avg `-0.0006` n `20`; unknown avg `6.0374` n `1266`
- 1h: commodity avg `0.0619` n `13`; crypto_alt avg `0.1068` n `239`; crypto_major avg `0.2448` n `8`; equity avg `-0.065` n `162`; fx avg `0.0188` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0019` n `20`; unknown avg `0.1716` n `1256`
- 4h: commodity avg `-0.228` n `13`; crypto_alt avg `0.3734` n `239`; crypto_major avg `0.926` n `8`; equity avg `-0.1721` n `162`; fx avg `0.011` n `6`; index avg `-0.0635` n `27`; metal avg `0.048` n `20`; unknown avg `4.8934` n `1216`
- 24h: commodity avg `-1.132` n `13`; crypto_alt avg `-0.1794` n `239`; crypto_major avg `0.2603` n `8`; equity avg `-3.3987` n `162`; fx avg `-0.1057` n `6`; index avg `-0.3331` n `27`; metal avg `-0.346` n `20`; unknown avg `500.8835` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
