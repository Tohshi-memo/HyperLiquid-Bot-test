# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T09:29:04.723356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `12`; crypto_alt avg `-0.0046` n `228`; crypto_major avg `-0.0213` n `8`; equity avg `0.0335` n `67`; fx avg `0.0` n `6`; index avg `0.0059` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.0722` n `396`
- 1h: commodity avg `0.0618` n `12`; crypto_alt avg `0.1689` n `228`; crypto_major avg `0.0749` n `8`; equity avg `0.1024` n `67`; fx avg `0.0035` n `6`; index avg `-0.0058` n `23`; metal avg `-0.0032` n `18`; unknown avg `1.2725` n `386`
- 4h: commodity avg `-0.0824` n `12`; crypto_alt avg `-1.6379` n `228`; crypto_major avg `-1.0867` n `8`; equity avg `-0.197` n `67`; fx avg `-0.0242` n `6`; index avg `-0.1237` n `23`; metal avg `0.0062` n `18`; unknown avg `0.8191` n `376`
- 24h: commodity avg `-0.4619` n `12`; crypto_alt avg `-5.9544` n `228`; crypto_major avg `-4.1592` n `8`; equity avg `-1.797` n `67`; fx avg `0.0329` n `6`; index avg `-0.2173` n `23`; metal avg `-0.3277` n `18`; unknown avg `-1.1243` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
