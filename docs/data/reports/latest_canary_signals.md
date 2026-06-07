# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T04:22:26.943710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.2105` n `228`; crypto_major avg `-0.1429` n `8`; equity avg `0.051` n `74`; fx avg `-0.0029` n `6`; index avg `-0.0277` n `23`; metal avg `-0.021` n `18`; unknown avg `-0.0293` n `516`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `-0.5469` n `228`; crypto_major avg `-0.4709` n `8`; equity avg `0.0351` n `74`; fx avg `0.0051` n `6`; index avg `0.1066` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.1217` n `516`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `1.0928` n `228`; crypto_major avg `1.3587` n `8`; equity avg `0.4957` n `74`; fx avg `0.0041` n `6`; index avg `0.3235` n `23`; metal avg `0.3892` n `18`; unknown avg `0.8569` n `516`
- 24h: commodity avg `0.1919` n `12`; crypto_alt avg `3.7474` n `228`; crypto_major avg `2.5378` n `8`; equity avg `1.8108` n `74`; fx avg `0.0314` n `6`; index avg `0.8724` n `23`; metal avg `0.6258` n `18`; unknown avg `0.7986` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
