# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T08:22:26.554843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.1054` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2392` n `12`; crypto_alt avg `-0.0628` n `228`; crypto_major avg `-0.2729` n `8`; equity avg `0.0172` n `72`; fx avg `-0.0112` n `6`; index avg `0.0109` n `23`; metal avg `-0.043` n `18`; unknown avg `0.7248` n `420`
- 1h: commodity avg `0.4539` n `12`; crypto_alt avg `-0.179` n `228`; crypto_major avg `-0.2594` n `8`; equity avg `-0.1568` n `72`; fx avg `-0.0401` n `6`; index avg `-0.0265` n `23`; metal avg `-0.249` n `18`; unknown avg `0.8247` n `420`
- 4h: commodity avg `0.7265` n `12`; crypto_alt avg `2.359` n `228`; crypto_major avg `1.2831` n `8`; equity avg `0.0244` n `72`; fx avg `0.0287` n `6`; index avg `-0.0239` n `23`; metal avg `-0.8223` n `18`; unknown avg `0.792` n `410`
- 24h: commodity avg `1.879` n `12`; crypto_alt avg `-1.236` n `228`; crypto_major avg `-3.5177` n `8`; equity avg `0.5038` n `72`; fx avg `0.0227` n `6`; index avg `0.8717` n `23`; metal avg `-1.9835` n `18`; unknown avg `1.2848` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
