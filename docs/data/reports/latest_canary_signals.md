# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T03:37:28.192122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2328` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.058` n `230`; crypto_major avg `-0.0508` n `8`; equity avg `-0.0885` n `102`; fx avg `-0.0246` n `6`; index avg `-0.026` n `25`; metal avg `0.062` n `20`; unknown avg `0.0585` n `779`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.0839` n `230`; crypto_major avg `0.0933` n `8`; equity avg `0.3192` n `102`; fx avg `0.0471` n `6`; index avg `0.0658` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.5342` n `779`
- 4h: commodity avg `-0.2445` n `12`; crypto_alt avg `-0.6045` n `230`; crypto_major avg `-1.0005` n `8`; equity avg `0.3686` n `102`; fx avg `0.1949` n `6`; index avg `0.2323` n `25`; metal avg `-0.2374` n `20`; unknown avg `1.275` n `779`
- 24h: commodity avg `-0.1343` n `12`; crypto_alt avg `-0.0484` n `230`; crypto_major avg `0.7089` n `8`; equity avg `8.0758` n `102`; fx avg `-0.1384` n `6`; index avg `1.1158` n `25`; metal avg `0.5431` n `20`; unknown avg `0.0708` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
