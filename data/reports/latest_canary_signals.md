# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T18:37:32.765226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.0962` n `228`; crypto_major avg `-0.1942` n `8`; equity avg `-0.0524` n `85`; fx avg `-0.0078` n `6`; index avg `-0.0179` n `23`; metal avg `-0.0177` n `20`; unknown avg `0.1126` n `717`
- 1h: commodity avg `-0.1155` n `12`; crypto_alt avg `0.3299` n `228`; crypto_major avg `0.7512` n `8`; equity avg `0.4201` n `85`; fx avg `-0.0049` n `6`; index avg `-0.0394` n `23`; metal avg `0.1245` n `20`; unknown avg `-0.046` n `717`
- 4h: commodity avg `-0.2116` n `12`; crypto_alt avg `-0.3538` n `228`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0973` n `85`; fx avg `-0.0413` n `6`; index avg `-0.0756` n `23`; metal avg `-0.0822` n `20`; unknown avg `-0.38` n `716`
- 24h: commodity avg `-1.0082` n `12`; crypto_alt avg `-0.2832` n `228`; crypto_major avg `0.2414` n `8`; equity avg `-0.1994` n `85`; fx avg `0.0374` n `6`; index avg `0.1122` n `23`; metal avg `0.2884` n `18`; unknown avg `0.727` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
