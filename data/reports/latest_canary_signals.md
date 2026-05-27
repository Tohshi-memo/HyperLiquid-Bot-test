# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T19:07:32.538116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.1797` n `228`; crypto_major avg `0.1216` n `8`; equity avg `-0.0985` n `67`; fx avg `0.0` n `6`; index avg `-0.0245` n `23`; metal avg `0.0451` n `18`; unknown avg `-0.1277` n `419`
- 1h: commodity avg `-0.3648` n `12`; crypto_alt avg `0.6901` n `228`; crypto_major avg `0.45` n `8`; equity avg `0.2184` n `67`; fx avg `0.0119` n `6`; index avg `0.1162` n `23`; metal avg `0.1897` n `18`; unknown avg `0.0341` n `418`
- 4h: commodity avg `-0.6896` n `12`; crypto_alt avg `-0.0187` n `228`; crypto_major avg `-0.2022` n `8`; equity avg `0.2133` n `67`; fx avg `0.0362` n `6`; index avg `0.2851` n `23`; metal avg `0.2911` n `18`; unknown avg `-0.3966` n `418`
- 24h: commodity avg `-1.3309` n `12`; crypto_alt avg `-0.1192` n `228`; crypto_major avg `-0.3174` n `8`; equity avg `-0.0909` n `67`; fx avg `-0.0698` n `6`; index avg `-0.4253` n `23`; metal avg `-1.0028` n `18`; unknown avg `-0.6162` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
