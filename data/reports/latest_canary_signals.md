# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T20:52:29.270922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.1282` n `235`; crypto_major avg `-0.0857` n `8`; equity avg `-0.0139` n `143`; fx avg `0.0053` n `6`; index avg `0.0012` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.0555` n `1079`
- 1h: commodity avg `0.0176` n `13`; crypto_alt avg `0.2906` n `235`; crypto_major avg `0.0304` n `8`; equity avg `0.0156` n `143`; fx avg `0.0085` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.3006` n `1071`
- 4h: commodity avg `-0.0807` n `13`; crypto_alt avg `0.4161` n `235`; crypto_major avg `0.1807` n `8`; equity avg `0.0835` n `143`; fx avg `-0.0022` n `6`; index avg `0.0131` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0809` n `1062`
- 24h: commodity avg `0.0102` n `13`; crypto_alt avg `2.9613` n `235`; crypto_major avg `1.4542` n `8`; equity avg `0.2086` n `143`; fx avg `-0.0156` n `6`; index avg `0.0433` n `26`; metal avg `0.0261` n `20`; unknown avg `-0.2319` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
