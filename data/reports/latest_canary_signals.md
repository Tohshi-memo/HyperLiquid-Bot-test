# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T14:22:40.308395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `13`; crypto_alt avg `-0.1485` n `238`; crypto_major avg `-0.121` n `8`; equity avg `-0.8693` n `156`; fx avg `0.0066` n `6`; index avg `-0.0807` n `27`; metal avg `-0.0662` n `20`; unknown avg `0.3382` n `1197`
- 1h: commodity avg `0.2123` n `13`; crypto_alt avg `-0.4419` n `238`; crypto_major avg `-0.649` n `8`; equity avg `-0.689` n `156`; fx avg `-0.0571` n `6`; index avg `-0.0791` n `27`; metal avg `-0.2177` n `20`; unknown avg `0.0403` n `1179`
- 4h: commodity avg `0.0183` n `13`; crypto_alt avg `-0.3475` n `238`; crypto_major avg `-0.7085` n `8`; equity avg `-1.3775` n `156`; fx avg `-0.1527` n `6`; index avg `-0.1143` n `27`; metal avg `-0.4269` n `20`; unknown avg `0.0124` n `1169`
- 24h: commodity avg `0.5598` n `13`; crypto_alt avg `-4.884` n `238`; crypto_major avg `-3.9167` n `8`; equity avg `-5.505` n `156`; fx avg `-0.0745` n `6`; index avg `-0.5013` n `27`; metal avg `-1.0065` n `20`; unknown avg `61.2643` n `992`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
