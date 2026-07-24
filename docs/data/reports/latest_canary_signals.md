# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T07:52:27.100501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.0192` n `230`; crypto_major avg `0.006` n `8`; equity avg `-0.026` n `100`; fx avg `-0.0052` n `6`; index avg `-0.011` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.0081` n `772`
- 1h: commodity avg `-0.0907` n `12`; crypto_alt avg `0.0784` n `230`; crypto_major avg `0.205` n `8`; equity avg `0.5002` n `100`; fx avg `0.0083` n `6`; index avg `0.1073` n `25`; metal avg `0.1449` n `20`; unknown avg `-0.0002` n `772`
- 4h: commodity avg `-0.3561` n `12`; crypto_alt avg `0.3078` n `230`; crypto_major avg `0.3236` n `8`; equity avg `0.5714` n `100`; fx avg `0.0351` n `6`; index avg `0.0956` n `25`; metal avg `0.168` n `20`; unknown avg `0.0833` n `756`
- 24h: commodity avg `-0.0568` n `12`; crypto_alt avg `-0.5796` n `230`; crypto_major avg `-0.8687` n `8`; equity avg `-1.278` n `99`; fx avg `-0.1115` n `6`; index avg `-0.3936` n `25`; metal avg `-0.4538` n `20`; unknown avg `0.1133` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0979`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0839`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0802`, n `666`, weak_sample_signal
