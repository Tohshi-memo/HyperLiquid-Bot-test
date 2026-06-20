# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T15:37:29.948462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `-0.0877` n `228`; crypto_major avg `-0.2105` n `8`; equity avg `-0.0653` n `78`; fx avg `0.0138` n `6`; index avg `0.0107` n `23`; metal avg `-0.0097` n `18`; unknown avg `0.0249` n `701`
- 1h: commodity avg `-0.0898` n `12`; crypto_alt avg `1.1906` n `228`; crypto_major avg `1.0277` n `8`; equity avg `0.2971` n `78`; fx avg `-0.001` n `6`; index avg `0.0323` n `23`; metal avg `0.0968` n `18`; unknown avg `1.4521` n `701`
- 4h: commodity avg `0.2729` n `12`; crypto_alt avg `0.3721` n `228`; crypto_major avg `0.1854` n `8`; equity avg `0.0903` n `78`; fx avg `0.0131` n `6`; index avg `0.009` n `23`; metal avg `0.0411` n `18`; unknown avg `0.7513` n `573`
- 24h: commodity avg `0.6479` n `12`; crypto_alt avg `-2.717` n `228`; crypto_major avg `-3.1652` n `8`; equity avg `1.2022` n `78`; fx avg `-0.0589` n `6`; index avg `0.3029` n `23`; metal avg `-4.0642` n `18`; unknown avg `-0.1346` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
