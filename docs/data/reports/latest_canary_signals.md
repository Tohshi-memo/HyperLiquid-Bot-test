# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T13:22:24.647478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1535` n `12`; crypto_alt avg `-0.1858` n `228`; crypto_major avg `-0.1015` n `8`; equity avg `-0.1417` n `67`; fx avg `0.0045` n `6`; index avg `-0.0916` n `23`; metal avg `-0.0571` n `18`; unknown avg `1.1594` n `418`
- 1h: commodity avg `0.4251` n `12`; crypto_alt avg `-0.7413` n `228`; crypto_major avg `-0.8674` n `8`; equity avg `-0.5752` n `67`; fx avg `0.0122` n `6`; index avg `-0.3598` n `23`; metal avg `-0.7106` n `18`; unknown avg `0.0646` n `418`
- 4h: commodity avg `0.3417` n `12`; crypto_alt avg `0.0145` n `228`; crypto_major avg `-0.383` n `8`; equity avg `-0.1637` n `67`; fx avg `-0.0012` n `6`; index avg `-0.0633` n `23`; metal avg `-0.9702` n `18`; unknown avg `0.5034` n `418`
- 24h: commodity avg `-1.5572` n `12`; crypto_alt avg `-2.065` n `228`; crypto_major avg `-1.1577` n `8`; equity avg `0.3282` n `67`; fx avg `-0.0512` n `6`; index avg `0.5314` n `23`; metal avg `-1.657` n `18`; unknown avg `1.0607` n `398`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
