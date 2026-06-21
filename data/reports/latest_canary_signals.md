# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T01:22:25.391925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.0098` n `228`; crypto_major avg `-0.0253` n `8`; equity avg `-0.0113` n `78`; fx avg `-0.0594` n `6`; index avg `-0.0068` n `23`; metal avg `0.0059` n `18`; unknown avg `0.1673` n `701`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0239` n `228`; crypto_major avg `-0.1075` n `8`; equity avg `-0.0296` n `78`; fx avg `-0.0562` n `6`; index avg `0.0006` n `23`; metal avg `-0.0181` n `18`; unknown avg `0.2623` n `701`
- 4h: commodity avg `0.0175` n `12`; crypto_alt avg `0.654` n `228`; crypto_major avg `0.396` n `8`; equity avg `0.1023` n `78`; fx avg `-0.0534` n `6`; index avg `0.0155` n `23`; metal avg `-0.0194` n `18`; unknown avg `0.8794` n `701`
- 24h: commodity avg `0.3957` n `12`; crypto_alt avg `1.2204` n `228`; crypto_major avg `1.4723` n `8`; equity avg `0.4225` n `78`; fx avg `-0.0097` n `6`; index avg `0.025` n `23`; metal avg `-0.0485` n `18`; unknown avg `0.5116` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
