# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T21:52:22.858429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3272` n `12`; crypto_alt avg `-0.1716` n `228`; crypto_major avg `-0.0` n `8`; equity avg `0.022` n `67`; fx avg `0.0081` n `6`; index avg `-0.0007` n `23`; metal avg `-0.023` n `18`; unknown avg `-0.0422` n `418`
- 1h: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.1034` n `228`; crypto_major avg `-0.08` n `8`; equity avg `0.1408` n `67`; fx avg `-0.0075` n `6`; index avg `0.0637` n `23`; metal avg `-0.0187` n `18`; unknown avg `-0.0939` n `418`
- 4h: commodity avg `-0.3533` n `12`; crypto_alt avg `-0.2302` n `228`; crypto_major avg `-0.4603` n `8`; equity avg `0.0425` n `67`; fx avg `0.0134` n `6`; index avg `0.111` n `23`; metal avg `0.4932` n `18`; unknown avg `-0.5526` n `418`
- 24h: commodity avg `0.2822` n `12`; crypto_alt avg `-1.9299` n `228`; crypto_major avg `-1.5643` n `8`; equity avg `-0.2744` n `67`; fx avg `-0.1223` n `6`; index avg `0.3553` n `23`; metal avg `-0.9006` n `18`; unknown avg `0.1078` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
