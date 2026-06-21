# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T06:22:25.596298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0696` n `228`; crypto_major avg `-0.0108` n `8`; equity avg `-0.015` n `78`; fx avg `-0.0001` n `6`; index avg `0.0046` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.0398` n `702`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0674` n `228`; crypto_major avg `-0.0334` n `8`; equity avg `0.0067` n `78`; fx avg `0.0015` n `6`; index avg `0.0012` n `23`; metal avg `0.0248` n `18`; unknown avg `-0.3943` n `670`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0192` n `228`; crypto_major avg `-0.3118` n `8`; equity avg `0.1505` n `78`; fx avg `0.0988` n `6`; index avg `0.0051` n `23`; metal avg `0.0427` n `18`; unknown avg `0.2311` n `662`
- 24h: commodity avg `0.1091` n `12`; crypto_alt avg `0.7116` n `228`; crypto_major avg `-0.0821` n `8`; equity avg `0.1653` n `78`; fx avg `0.0617` n `6`; index avg `-0.0029` n `23`; metal avg `0.0006` n `18`; unknown avg `-0.2873` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
