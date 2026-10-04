# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T16:37:32.391931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.0772` n `235`; crypto_major avg `0.154` n `8`; equity avg `0.0037` n `144`; fx avg `-0.009` n `6`; index avg `0.0026` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.1807` n `1078`
- 1h: commodity avg `-0.0601` n `13`; crypto_alt avg `-0.0595` n `235`; crypto_major avg `0.1485` n `8`; equity avg `-0.0088` n `144`; fx avg `-0.0262` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.2119` n `1070`
- 4h: commodity avg `-0.1002` n `13`; crypto_alt avg `0.0628` n `235`; crypto_major avg `0.1486` n `8`; equity avg `0.0137` n `144`; fx avg `-0.0022` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0182` n `20`; unknown avg `0.0158` n `1070`
- 24h: commodity avg `0.0444` n `13`; crypto_alt avg `0.8309` n `235`; crypto_major avg `1.0573` n `8`; equity avg `0.2292` n `144`; fx avg `0.0058` n `6`; index avg `-0.006` n `26`; metal avg `-0.0143` n `20`; unknown avg `-0.0008` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
