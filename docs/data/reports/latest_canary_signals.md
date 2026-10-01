# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T02:22:32.442079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2783` n `13`; crypto_alt avg `-0.0725` n `234`; crypto_major avg `-0.1367` n `8`; equity avg `0.0625` n `142`; fx avg `-0.0116` n `6`; index avg `0.0151` n `26`; metal avg `0.0228` n `20`; unknown avg `0.5934` n `974`
- 1h: commodity avg `0.365` n `13`; crypto_alt avg `-0.77` n `234`; crypto_major avg `-0.3887` n `8`; equity avg `0.0723` n `142`; fx avg `-0.0158` n `6`; index avg `0.0276` n `26`; metal avg `-0.0462` n `20`; unknown avg `0.4483` n `972`
- 4h: commodity avg `-0.0211` n `13`; crypto_alt avg `0.0228` n `234`; crypto_major avg `-0.3517` n `8`; equity avg `0.3078` n `142`; fx avg `0.0953` n `6`; index avg `0.1133` n `26`; metal avg `-0.0129` n `20`; unknown avg `1.2038` n `942`
- 24h: commodity avg `0.1647` n `13`; crypto_alt avg `0.2963` n `234`; crypto_major avg `0.4975` n `8`; equity avg `0.1342` n `142`; fx avg `0.2545` n `6`; index avg `0.1081` n `26`; metal avg `-0.1538` n `20`; unknown avg `774.4896` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
