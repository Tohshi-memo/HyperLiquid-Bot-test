# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T22:07:26.925811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.098` n `228`; crypto_major avg `-0.0069` n `8`; equity avg `-0.0391` n `88`; fx avg `-0.0052` n `6`; index avg `-0.042` n `23`; metal avg `-0.0011` n `20`; unknown avg `0.0082` n `764`
- 1h: commodity avg `0.1645` n `12`; crypto_alt avg `-0.4232` n `228`; crypto_major avg `-0.468` n `8`; equity avg `-0.0578` n `88`; fx avg `-0.0075` n `6`; index avg `-0.0578` n `23`; metal avg `-0.0184` n `20`; unknown avg `0.1406` n `764`
- 4h: commodity avg `0.1145` n `12`; crypto_alt avg `-0.7442` n `228`; crypto_major avg `-0.9066` n `8`; equity avg `-0.048` n `88`; fx avg `-0.0046` n `6`; index avg `-0.0493` n `23`; metal avg `-0.0372` n `20`; unknown avg `-0.0048` n `764`
- 24h: commodity avg `0.1717` n `12`; crypto_alt avg `-0.4641` n `228`; crypto_major avg `-0.5806` n `8`; equity avg `0.4047` n `88`; fx avg `0.0125` n `6`; index avg `-0.0317` n `23`; metal avg `-0.0175` n `20`; unknown avg `-0.2399` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
