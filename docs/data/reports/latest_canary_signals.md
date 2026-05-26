# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T15:22:38.675984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.0715` n `228`; crypto_major avg `-0.0335` n `8`; equity avg `0.0823` n `67`; fx avg `-0.0051` n `6`; index avg `-0.0518` n `23`; metal avg `-0.0253` n `18`; unknown avg `-0.3354` n `418`
- 1h: commodity avg `0.1254` n `12`; crypto_alt avg `-1.0772` n `228`; crypto_major avg `-1.0838` n `8`; equity avg `-0.1407` n `67`; fx avg `-0.0177` n `6`; index avg `-0.1257` n `23`; metal avg `-0.1756` n `18`; unknown avg `1.17` n `416`
- 4h: commodity avg `0.8808` n `12`; crypto_alt avg `-0.5058` n `228`; crypto_major avg `-0.1854` n `8`; equity avg `-0.0126` n `67`; fx avg `-0.0254` n `6`; index avg `0.2954` n `23`; metal avg `-0.2126` n `18`; unknown avg `-0.4724` n `415`
- 24h: commodity avg `1.2633` n `12`; crypto_alt avg `-0.7233` n `228`; crypto_major avg `-0.7223` n `8`; equity avg `-0.4392` n `67`; fx avg `-0.1601` n `6`; index avg `0.3462` n `23`; metal avg `-1.2696` n `18`; unknown avg `-0.6079` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
