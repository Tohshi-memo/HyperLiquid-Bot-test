# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T18:37:28.659064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.1492` n `228`; crypto_major avg `0.1343` n `8`; equity avg `0.0227` n `74`; fx avg `0.0023` n `6`; index avg `0.0034` n `23`; metal avg `-0.0052` n `18`; unknown avg `-0.2549` n `645`
- 1h: commodity avg `0.1341` n `12`; crypto_alt avg `-0.3398` n `228`; crypto_major avg `-0.189` n `8`; equity avg `-0.0725` n `74`; fx avg `-0.0051` n `6`; index avg `-0.0012` n `23`; metal avg `-0.0165` n `18`; unknown avg `-0.5586` n `645`
- 4h: commodity avg `-0.1548` n `12`; crypto_alt avg `0.1486` n `228`; crypto_major avg `0.0476` n `8`; equity avg `0.109` n `74`; fx avg `-0.0121` n `6`; index avg `0.0571` n `23`; metal avg `0.0383` n `18`; unknown avg `-0.3975` n `645`
- 24h: commodity avg `0.0894` n `12`; crypto_alt avg `-1.5806` n `228`; crypto_major avg `-0.82` n `8`; equity avg `0.2206` n `74`; fx avg `-0.0523` n `6`; index avg `0.2297` n `23`; metal avg `-0.0923` n `18`; unknown avg `0.8809` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
