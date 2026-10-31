# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T00:22:26.678818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.1926` n `238`; crypto_major avg `0.131` n `8`; equity avg `-0.0081` n `156`; fx avg `-0.0048` n `6`; index avg `0.0065` n `27`; metal avg `0.0127` n `20`; unknown avg `0.0251` n `1262`
- 1h: commodity avg `-0.034` n `13`; crypto_alt avg `0.5004` n `238`; crypto_major avg `0.5021` n `8`; equity avg `0.0735` n `156`; fx avg `0.0077` n `6`; index avg `0.0101` n `27`; metal avg `0.0181` n `20`; unknown avg `128.9282` n `1250`
- 4h: commodity avg `-0.1381` n `13`; crypto_alt avg `1.7558` n `238`; crypto_major avg `0.8059` n `8`; equity avg `0.2354` n `156`; fx avg `-0.0168` n `6`; index avg `0.0243` n `27`; metal avg `0.0523` n `20`; unknown avg `0.2854` n `1223`
- 24h: commodity avg `0.0144` n `13`; crypto_alt avg `5.4979` n `238`; crypto_major avg `2.0554` n `8`; equity avg `-2.3607` n `156`; fx avg `-0.1224` n `6`; index avg `-0.2062` n `27`; metal avg `-0.8553` n `20`; unknown avg `4.5211` n `1020`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
