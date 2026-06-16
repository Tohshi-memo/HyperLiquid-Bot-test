# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T06:52:34.488003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1249` n `12`; crypto_alt avg `-0.1021` n `228`; crypto_major avg `0.0845` n `8`; equity avg `0.0112` n `77`; fx avg `-0.0403` n `6`; index avg `-0.0281` n `23`; metal avg `-0.0061` n `18`; unknown avg `0.0748` n `687`
- 1h: commodity avg `0.3564` n `12`; crypto_alt avg `0.2615` n `228`; crypto_major avg `0.5017` n `8`; equity avg `0.2365` n `77`; fx avg `-0.0444` n `6`; index avg `0.0117` n `23`; metal avg `0.0903` n `18`; unknown avg `0.5553` n `647`
- 4h: commodity avg `0.1749` n `12`; crypto_alt avg `1.1427` n `228`; crypto_major avg `1.5459` n `8`; equity avg `0.5998` n `77`; fx avg `-0.059` n `6`; index avg `0.0486` n `23`; metal avg `0.1799` n `18`; unknown avg `0.8227` n `647`
- 24h: commodity avg `0.5777` n `12`; crypto_alt avg `0.5318` n `228`; crypto_major avg `2.7444` n `8`; equity avg `1.338` n `76`; fx avg `-0.1562` n `6`; index avg `0.4032` n `23`; metal avg `-0.045` n `18`; unknown avg `1.7006` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
