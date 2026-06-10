# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T08:22:29.904194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1185` n `12`; crypto_alt avg `0.104` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `-0.1856` n `74`; fx avg `-0.0172` n `6`; index avg `-0.0736` n `23`; metal avg `0.0529` n `18`; unknown avg `0.2345` n `547`
- 1h: commodity avg `0.3801` n `12`; crypto_alt avg `-0.3151` n `228`; crypto_major avg `-0.2245` n `8`; equity avg `-0.4688` n `74`; fx avg `-0.0247` n `6`; index avg `-0.2619` n `23`; metal avg `-0.5007` n `18`; unknown avg `0.2564` n `547`
- 4h: commodity avg `0.2514` n `12`; crypto_alt avg `-0.0248` n `228`; crypto_major avg `-0.2325` n `8`; equity avg `-0.1546` n `74`; fx avg `0.0415` n `6`; index avg `-0.2208` n `23`; metal avg `0.0477` n `18`; unknown avg `-0.1019` n `537`
- 24h: commodity avg `-0.3749` n `12`; crypto_alt avg `-1.3818` n `228`; crypto_major avg `-3.5818` n `8`; equity avg `-3.9135` n `74`; fx avg `0.1033` n `6`; index avg `-2.0685` n `23`; metal avg `-3.521` n `18`; unknown avg `0.1463` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
