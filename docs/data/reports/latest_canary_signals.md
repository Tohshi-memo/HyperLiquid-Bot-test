# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T22:22:24.070884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.039` n `230`; crypto_major avg `-0.0616` n `8`; equity avg `-0.0477` n `98`; fx avg `-0.0017` n `6`; index avg `0.0058` n `25`; metal avg `-0.0274` n `20`; unknown avg `1.3012` n `770`
- 1h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.387` n `230`; crypto_major avg `-0.3693` n `8`; equity avg `-0.0281` n `98`; fx avg `-0.0229` n `6`; index avg `-0.0285` n `25`; metal avg `-0.0534` n `20`; unknown avg `1.864` n `770`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `-0.3345` n `230`; crypto_major avg `-0.4732` n `8`; equity avg `-0.872` n `98`; fx avg `-0.0465` n `6`; index avg `-0.1824` n `25`; metal avg `-0.0972` n `20`; unknown avg `0.1679` n `770`
- 24h: commodity avg `-0.4076` n `12`; crypto_alt avg `1.1749` n `230`; crypto_major avg `0.768` n `8`; equity avg `-0.4912` n `98`; fx avg `-0.1925` n `6`; index avg `-0.0659` n `25`; metal avg `0.1797` n `20`; unknown avg `0.2457` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0948`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
