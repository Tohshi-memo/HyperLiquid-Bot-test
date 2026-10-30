# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T20:37:36.974025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `13`; crypto_alt avg `0.0775` n `238`; crypto_major avg `0.1593` n `8`; equity avg `-0.0173` n `156`; fx avg `0.0064` n `6`; index avg `-0.0193` n `27`; metal avg `-0.0256` n `20`; unknown avg `1.0097` n `1249`
- 1h: commodity avg `-0.1083` n `13`; crypto_alt avg `0.178` n `238`; crypto_major avg `0.2235` n `8`; equity avg `0.6114` n `156`; fx avg `-0.0176` n `6`; index avg `0.0549` n `27`; metal avg `0.0167` n `20`; unknown avg `1.6806` n `1163`
- 4h: commodity avg `-0.1699` n `13`; crypto_alt avg `-0.3231` n `238`; crypto_major avg `-0.4511` n `8`; equity avg `0.0658` n `156`; fx avg `-0.0002` n `6`; index avg `-0.0282` n `27`; metal avg `-0.1406` n `20`; unknown avg `1.0286` n `1165`
- 24h: commodity avg `0.1024` n `13`; crypto_alt avg `-2.3286` n `238`; crypto_major avg `-2.1535` n `8`; equity avg `-4.1944` n `156`; fx avg `-0.108` n `6`; index avg `-0.3907` n `27`; metal avg `-1.0796` n `20`; unknown avg `1.8324` n `1020`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
