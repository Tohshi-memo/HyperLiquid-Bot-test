# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T02:22:16.699493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.205` n `228`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0146` n `67`; fx avg `-0.0082` n `6`; index avg `0.038` n `23`; metal avg `0.0182` n `18`; unknown avg `0.7922` n `418`
- 1h: commodity avg `-0.2316` n `12`; crypto_alt avg `-0.6889` n `228`; crypto_major avg `-0.277` n `8`; equity avg `-0.0835` n `67`; fx avg `-0.0151` n `6`; index avg `-0.0001` n `23`; metal avg `-0.3662` n `18`; unknown avg `0.8018` n `418`
- 4h: commodity avg `-0.3624` n `12`; crypto_alt avg `-0.4062` n `228`; crypto_major avg `0.0235` n `8`; equity avg `0.1411` n `67`; fx avg `-0.0386` n `6`; index avg `0.2554` n `23`; metal avg `-0.2417` n `18`; unknown avg `0.4479` n `418`
- 24h: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.6087` n `228`; crypto_major avg `-0.457` n `8`; equity avg `0.8218` n `67`; fx avg `-0.0622` n `6`; index avg `1.0268` n `23`; metal avg `-0.1708` n `18`; unknown avg `0.6114` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
