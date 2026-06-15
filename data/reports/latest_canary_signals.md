# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T22:22:43.736522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.1257` n `228`; crypto_major avg `-0.2177` n `8`; equity avg `-0.1437` n `77`; fx avg `-0.0226` n `6`; index avg `-0.0729` n `23`; metal avg `-0.0442` n `18`; unknown avg `0.9174` n `687`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.2161` n `228`; crypto_major avg `-0.3296` n `8`; equity avg `-0.0621` n `77`; fx avg `-0.0066` n `6`; index avg `-0.0854` n `23`; metal avg `-0.0036` n `18`; unknown avg `0.1515` n `687`
- 4h: commodity avg `0.1742` n `12`; crypto_alt avg `-1.1061` n `228`; crypto_major avg `-0.9689` n `8`; equity avg `-0.1965` n `77`; fx avg `-0.0253` n `6`; index avg `-0.1286` n `23`; metal avg `-0.2607` n `18`; unknown avg `0.3242` n `679`
- 24h: commodity avg `0.2724` n `12`; crypto_alt avg `1.8884` n `228`; crypto_major avg `3.3257` n `8`; equity avg `1.6432` n `76`; fx avg `-0.0818` n `6`; index avg `0.8245` n `23`; metal avg `0.1458` n `18`; unknown avg `2.5791` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
