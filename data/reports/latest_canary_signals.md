# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T23:07:28.614088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0905` n `13`; crypto_alt avg `0.1807` n `238`; crypto_major avg `0.0614` n `8`; equity avg `-0.1607` n `156`; fx avg `0.0262` n `6`; index avg `-0.0402` n `27`; metal avg `0.0265` n `20`; unknown avg `96.9603` n `1255`
- 1h: commodity avg `-0.0508` n `13`; crypto_alt avg `-0.0359` n `238`; crypto_major avg `-0.0714` n `8`; equity avg `-0.2127` n `156`; fx avg `0.0278` n `6`; index avg `-0.0216` n `27`; metal avg `0.0217` n `20`; unknown avg `0.2357` n `1237`
- 4h: commodity avg `-0.0354` n `13`; crypto_alt avg `-0.0186` n `238`; crypto_major avg `-0.1192` n `8`; equity avg `-0.1786` n `156`; fx avg `0.0066` n `6`; index avg `-0.0521` n `27`; metal avg `0.0066` n `20`; unknown avg `1.4831` n `1191`
- 24h: commodity avg `-0.0362` n `13`; crypto_alt avg `-0.5535` n `238`; crypto_major avg `-0.151` n `8`; equity avg `0.1295` n `156`; fx avg `0.0213` n `6`; index avg `0.0114` n `27`; metal avg `0.049` n `20`; unknown avg `3.7655` n `1084`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
