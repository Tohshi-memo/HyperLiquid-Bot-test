# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T18:22:26.008234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1427` n `13`; crypto_alt avg `-0.367` n `237`; crypto_major avg `-0.3333` n `8`; equity avg `0.0065` n `151`; fx avg `-0.001` n `6`; index avg `0.0031` n `26`; metal avg `-0.0053` n `20`; unknown avg `-0.0813` n `1196`
- 1h: commodity avg `-0.14` n `13`; crypto_alt avg `-0.4871` n `237`; crypto_major avg `-0.3169` n `8`; equity avg `-0.2846` n `151`; fx avg `0.0019` n `6`; index avg `-0.0176` n `26`; metal avg `0.0671` n `20`; unknown avg `0.2118` n `1194`
- 4h: commodity avg `0.2556` n `13`; crypto_alt avg `-0.1006` n `237`; crypto_major avg `-0.1627` n `8`; equity avg `-0.617` n `151`; fx avg `0.0113` n `6`; index avg `-0.107` n `26`; metal avg `0.0551` n `20`; unknown avg `2.526` n `1185`
- 24h: commodity avg `-0.1461` n `13`; crypto_alt avg `1.1669` n `237`; crypto_major avg `1.332` n `8`; equity avg `2.643` n `151`; fx avg `-0.0327` n `6`; index avg `0.5473` n `26`; metal avg `0.1429` n `20`; unknown avg `3.6485` n `918`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
