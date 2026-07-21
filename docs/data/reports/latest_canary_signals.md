# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T21:52:27.110390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `0.0022` n `8`; equity avg `-0.0077` n `98`; fx avg `0.0093` n `6`; index avg `0.0005` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.015` n `771`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `0.118` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.2652` n `98`; fx avg `-0.0246` n `6`; index avg `0.0487` n `25`; metal avg `0.0147` n `20`; unknown avg `0.0151` n `771`
- 4h: commodity avg `0.1358` n `12`; crypto_alt avg `0.4103` n `230`; crypto_major avg `0.0917` n `8`; equity avg `0.5253` n `98`; fx avg `-0.0065` n `6`; index avg `0.0208` n `25`; metal avg `0.0514` n `20`; unknown avg `-0.0258` n `771`
- 24h: commodity avg `0.4873` n `12`; crypto_alt avg `0.9199` n `230`; crypto_major avg `0.6416` n `8`; equity avg `4.4172` n `98`; fx avg `0.0511` n `6`; index avg `0.6612` n `25`; metal avg `0.723` n `20`; unknown avg `0.275` n `754`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0896`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
