# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T12:07:26.673189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0768` n `12`; crypto_alt avg `-0.2358` n `228`; crypto_major avg `-0.2906` n `8`; equity avg `-0.1466` n `69`; fx avg `-0.0002` n `6`; index avg `-0.0271` n `23`; metal avg `-0.0006` n `18`; unknown avg `0.7959` n `422`
- 1h: commodity avg `-0.2697` n `12`; crypto_alt avg `-0.3951` n `228`; crypto_major avg `-0.2764` n `8`; equity avg `-0.2447` n `69`; fx avg `0.0011` n `6`; index avg `-0.0499` n `23`; metal avg `0.1506` n `18`; unknown avg `1.4033` n `416`
- 4h: commodity avg `-0.4453` n `12`; crypto_alt avg `-0.1002` n `228`; crypto_major avg `0.115` n `8`; equity avg `-0.2262` n `69`; fx avg `-0.009` n `6`; index avg `-0.0763` n `23`; metal avg `0.2879` n `18`; unknown avg `1.8051` n `416`
- 24h: commodity avg `0.649` n `12`; crypto_alt avg `-0.7278` n `228`; crypto_major avg `-0.7303` n `8`; equity avg `-0.3867` n `69`; fx avg `-0.0079` n `6`; index avg `0.4925` n `23`; metal avg `0.3423` n `18`; unknown avg `3.3217` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2886`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
