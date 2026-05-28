# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T13:22:22.277777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1321` n `12`; crypto_alt avg `-0.1523` n `228`; crypto_major avg `-0.2087` n `8`; equity avg `-0.0796` n `67`; fx avg `-0.0066` n `6`; index avg `-0.1083` n `23`; metal avg `-0.1179` n `18`; unknown avg `-0.0746` n `419`
- 1h: commodity avg `-0.1565` n `12`; crypto_alt avg `0.3641` n `228`; crypto_major avg `0.1784` n `8`; equity avg `0.4257` n `67`; fx avg `0.0508` n `6`; index avg `0.1849` n `23`; metal avg `0.7797` n `18`; unknown avg `-0.0352` n `419`
- 4h: commodity avg `0.3099` n `12`; crypto_alt avg `-0.3793` n `228`; crypto_major avg `-0.2404` n `8`; equity avg `0.186` n `67`; fx avg `0.0794` n `6`; index avg `0.0908` n `23`; metal avg `0.1289` n `18`; unknown avg `-0.334` n `419`
- 24h: commodity avg `0.7937` n `12`; crypto_alt avg `-5.125` n `228`; crypto_major avg `-3.6088` n `8`; equity avg `-1.0372` n `67`; fx avg `-0.008` n `6`; index avg `-0.788` n `23`; metal avg `-0.5153` n `18`; unknown avg `-1.9258` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
