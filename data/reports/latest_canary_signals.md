# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T07:37:27.762421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.2814` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `-0.0208` n `78`; fx avg `-0.098` n `6`; index avg `-0.011` n `23`; metal avg `0.0036` n `18`; unknown avg `-0.0356` n `702`
- 1h: commodity avg `-0.0599` n `12`; crypto_alt avg `0.2482` n `228`; crypto_major avg `-0.0836` n `8`; equity avg `0.0403` n `78`; fx avg `-0.1005` n `6`; index avg `0.0216` n `23`; metal avg `0.0095` n `18`; unknown avg `0.3633` n `702`
- 4h: commodity avg `-0.0658` n `12`; crypto_alt avg `0.3462` n `228`; crypto_major avg `-0.3162` n `8`; equity avg `0.1716` n `78`; fx avg `-0.1019` n `6`; index avg `0.0217` n `23`; metal avg `0.0593` n `18`; unknown avg `0.2854` n `662`
- 24h: commodity avg `0.0329` n `12`; crypto_alt avg `1.3157` n `228`; crypto_major avg `0.1025` n `8`; equity avg `0.3316` n `78`; fx avg `0.2492` n `6`; index avg `0.0384` n `23`; metal avg `0.0044` n `18`; unknown avg `-0.1218` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
