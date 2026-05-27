# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T15:37:23.554809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2129` n `12`; crypto_alt avg `0.3912` n `228`; crypto_major avg `0.3639` n `8`; equity avg `0.0675` n `67`; fx avg `0.0089` n `6`; index avg `0.0483` n `23`; metal avg `0.1299` n `18`; unknown avg `1.0444` n `418`
- 1h: commodity avg `0.101` n `12`; crypto_alt avg `1.4614` n `228`; crypto_major avg `0.9933` n `8`; equity avg `-0.2522` n `67`; fx avg `-0.0438` n `6`; index avg `0.0732` n `23`; metal avg `-0.0576` n `18`; unknown avg `0.2471` n `418`
- 4h: commodity avg `0.2554` n `12`; crypto_alt avg `0.808` n `228`; crypto_major avg `-0.1798` n `8`; equity avg `-1.2336` n `67`; fx avg `-0.0315` n `6`; index avg `-0.9909` n `23`; metal avg `0.0494` n `18`; unknown avg `0.7413` n `418`
- 24h: commodity avg `-1.3624` n `12`; crypto_alt avg `-0.4139` n `228`; crypto_major avg `-0.5273` n `8`; equity avg `-0.4768` n `67`; fx avg `-0.04` n `6`; index avg `-0.4522` n `23`; metal avg `-0.957` n `18`; unknown avg `1.4479` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
