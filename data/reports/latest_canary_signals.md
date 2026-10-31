# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T10:07:28.326881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.0741` n `238`; crypto_major avg `0.0042` n `8`; equity avg `-0.0173` n `156`; fx avg `0.0061` n `6`; index avg `-0.003` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.1` n `1256`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `-0.1814` n `238`; crypto_major avg `-0.0994` n `8`; equity avg `0.0017` n `156`; fx avg `-0.0003` n `6`; index avg `-0.0006` n `27`; metal avg `0.0133` n `20`; unknown avg `-0.1544` n `1256`
- 4h: commodity avg `-0.0494` n `13`; crypto_alt avg `-0.2533` n `238`; crypto_major avg `-0.352` n `8`; equity avg `-0.0469` n `156`; fx avg `0.0046` n `6`; index avg `-0.0083` n `27`; metal avg `0.0068` n `20`; unknown avg `5.0619` n `1232`
- 24h: commodity avg `-0.2962` n `13`; crypto_alt avg `0.6213` n `238`; crypto_major avg `-0.6526` n `8`; equity avg `-1.6612` n `156`; fx avg `-0.1146` n `6`; index avg `-0.1487` n `27`; metal avg `-0.4251` n `20`; unknown avg `4.747` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
