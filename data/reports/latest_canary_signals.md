# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T03:52:26.870086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `0.0471` n `230`; crypto_major avg `0.0221` n `8`; equity avg `0.1896` n `98`; fx avg `-0.0207` n `6`; index avg `0.0411` n `25`; metal avg `0.0218` n `20`; unknown avg `0.0094` n `771`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.4705` n `230`; crypto_major avg `0.3965` n `8`; equity avg `1.0136` n `98`; fx avg `-0.0345` n `6`; index avg `0.1416` n `25`; metal avg `0.1108` n `20`; unknown avg `2.4378` n `771`
- 4h: commodity avg `-0.0376` n `12`; crypto_alt avg `0.6798` n `230`; crypto_major avg `0.6715` n `8`; equity avg `1.4765` n `98`; fx avg `-0.0103` n `6`; index avg `0.3897` n `25`; metal avg `0.3646` n `20`; unknown avg `0.4749` n `770`
- 24h: commodity avg `-0.3296` n `12`; crypto_alt avg `1.8298` n `230`; crypto_major avg `1.4915` n `8`; equity avg `1.004` n `98`; fx avg `-0.1436` n `6`; index avg `0.239` n `25`; metal avg `0.2556` n `20`; unknown avg `0.0339` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0865`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
