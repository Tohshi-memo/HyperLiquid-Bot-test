# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T09:37:29.386825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `-0.2103` n `235`; crypto_major avg `-0.0153` n `8`; equity avg `-0.0012` n `143`; fx avg `0.002` n `6`; index avg `0.0003` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.2167` n `1079`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `-0.2838` n `235`; crypto_major avg `0.1052` n `8`; equity avg `0.0228` n `143`; fx avg `0.002` n `6`; index avg `0.0057` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.4027` n `1077`
- 4h: commodity avg `-0.003` n `13`; crypto_alt avg `-0.1232` n `235`; crypto_major avg `0.4006` n `8`; equity avg `-0.0078` n `143`; fx avg `0.0044` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.2965` n `1033`
- 24h: commodity avg `0.1504` n `13`; crypto_alt avg `2.415` n `235`; crypto_major avg `1.4046` n `8`; equity avg `0.2542` n `143`; fx avg `-0.03` n `6`; index avg `0.0199` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.1331` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
