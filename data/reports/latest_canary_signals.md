# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T08:37:27.340100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.0144` n `234`; crypto_major avg `-0.0378` n `8`; equity avg `-0.007` n `140`; fx avg `-0.014` n `6`; index avg `0.0273` n `26`; metal avg `0.0042` n `20`; unknown avg `4.5911` n `942`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `0.709` n `234`; crypto_major avg `0.3421` n `8`; equity avg `0.0429` n `140`; fx avg `-0.0175` n `6`; index avg `0.0126` n `26`; metal avg `0.0013` n `20`; unknown avg `4.5624` n `934`
- 4h: commodity avg `0.0225` n `12`; crypto_alt avg `0.2668` n `234`; crypto_major avg `0.3592` n `8`; equity avg `-0.0098` n `140`; fx avg `-0.0146` n `6`; index avg `-0.0` n `26`; metal avg `-0.007` n `20`; unknown avg `5.0676` n `898`
- 24h: commodity avg `0.2133` n `12`; crypto_alt avg `3.3461` n `234`; crypto_major avg `4.1108` n `8`; equity avg `0.0586` n `140`; fx avg `-0.0418` n `6`; index avg `-0.053` n `26`; metal avg `-0.2049` n `20`; unknown avg `5.5083` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
