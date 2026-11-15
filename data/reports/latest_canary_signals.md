# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T20:52:31.363374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `13`; crypto_alt avg `-0.0161` n `239`; crypto_major avg `0.0785` n `8`; equity avg `0.0453` n `162`; fx avg `-0.0006` n `6`; index avg `0.0043` n `27`; metal avg `0.0209` n `20`; unknown avg `0.2278` n `1265`
- 1h: commodity avg `-0.0031` n `13`; crypto_alt avg `0.2656` n `239`; crypto_major avg `0.2966` n `8`; equity avg `0.0735` n `162`; fx avg `0.0099` n `6`; index avg `0.0006` n `27`; metal avg `0.0492` n `20`; unknown avg `-0.058` n `1255`
- 4h: commodity avg `0.0352` n `13`; crypto_alt avg `0.8298` n `239`; crypto_major avg `0.9468` n `8`; equity avg `0.3292` n `162`; fx avg `0.0519` n `6`; index avg `0.028` n `27`; metal avg `0.139` n `20`; unknown avg `2.6892` n `1251`
- 24h: commodity avg `0.0665` n `13`; crypto_alt avg `1.9284` n `239`; crypto_major avg `1.8096` n `8`; equity avg `1.0476` n `162`; fx avg `0.0414` n `6`; index avg `0.1041` n `27`; metal avg `0.1288` n `20`; unknown avg `3.2605` n `1154`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
