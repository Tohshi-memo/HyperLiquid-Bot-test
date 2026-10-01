# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T21:07:48.411153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `13`; crypto_alt avg `-0.1205` n `234`; crypto_major avg `-0.0284` n `8`; equity avg `0.0004` n `142`; fx avg `-0.0064` n `6`; index avg `0.001` n `26`; metal avg `0.0104` n `20`; unknown avg `-0.1265` n `981`
- 1h: commodity avg `-0.033` n `13`; crypto_alt avg `-0.1563` n `234`; crypto_major avg `-0.1675` n `8`; equity avg `0.0309` n `142`; fx avg `-0.0174` n `6`; index avg `-0.0021` n `26`; metal avg `0.0079` n `20`; unknown avg `3.124` n `939`
- 4h: commodity avg `0.1336` n `13`; crypto_alt avg `0.6398` n `234`; crypto_major avg `0.2977` n `8`; equity avg `0.6741` n `142`; fx avg `0.0265` n `6`; index avg `0.1494` n `26`; metal avg `0.117` n `20`; unknown avg `0.5931` n `931`
- 24h: commodity avg `0.0505` n `13`; crypto_alt avg `0.1684` n `234`; crypto_major avg `-0.0505` n `8`; equity avg `1.1474` n `142`; fx avg `-0.1208` n `6`; index avg `0.2279` n `26`; metal avg `-0.0307` n `20`; unknown avg `0.496` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
