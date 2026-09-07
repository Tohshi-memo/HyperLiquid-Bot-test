# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T22:07:31.819397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `-0.0464` n `232`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0506` n `134`; fx avg `0.0079` n `6`; index avg `-0.0143` n `26`; metal avg `0.0014` n `20`; unknown avg `0.2239` n `794`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `-0.1813` n `232`; crypto_major avg `-0.0727` n `8`; equity avg `-0.0337` n `134`; fx avg `0.0122` n `6`; index avg `-0.01` n `26`; metal avg `0.0108` n `20`; unknown avg `1.4898` n `794`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `0.0915` n `232`; crypto_major avg `-0.0731` n `8`; equity avg `0.0154` n `134`; fx avg `0.0004` n `6`; index avg `0.0025` n `26`; metal avg `0.0424` n `20`; unknown avg `7.251` n `752`
- 24h: commodity avg `0.1909` n `12`; crypto_alt avg `0.1231` n `232`; crypto_major avg `-0.9954` n `8`; equity avg `0.4501` n `134`; fx avg `-0.1371` n `6`; index avg `0.0712` n `26`; metal avg `0.1048` n `20`; unknown avg `7800.9919` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
