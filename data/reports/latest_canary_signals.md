# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T16:37:35.212991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0735` n `13`; crypto_alt avg `0.103` n `239`; crypto_major avg `0.2258` n `8`; equity avg `0.6136` n `165`; fx avg `0.0054` n `6`; index avg `0.0611` n `27`; metal avg `0.0753` n `20`; unknown avg `0.9316` n `1265`
- 1h: commodity avg `0.0694` n `13`; crypto_alt avg `-0.1774` n `239`; crypto_major avg `0.0525` n `8`; equity avg `1.3731` n `165`; fx avg `0.038` n `6`; index avg `0.1278` n `27`; metal avg `0.0298` n `20`; unknown avg `24.3925` n `1257`
- 4h: commodity avg `-0.0365` n `13`; crypto_alt avg `-0.8612` n `239`; crypto_major avg `-0.7377` n `8`; equity avg `-0.9323` n `165`; fx avg `0.0054` n `6`; index avg `-0.1903` n `27`; metal avg `-0.2838` n `20`; unknown avg `14.7249` n `1257`
- 24h: commodity avg `0.2324` n `13`; crypto_alt avg `0.6005` n `239`; crypto_major avg `1.3267` n `8`; equity avg `2.2761` n `165`; fx avg `0.0649` n `6`; index avg `0.292` n `27`; metal avg `-0.264` n `20`; unknown avg `4.2132` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
