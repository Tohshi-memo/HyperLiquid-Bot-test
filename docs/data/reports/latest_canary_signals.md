# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T12:37:26.930583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1287` n `12`; crypto_alt avg `-0.409` n `228`; crypto_major avg `-0.3412` n `8`; equity avg `-0.0383` n `74`; fx avg `0.0014` n `6`; index avg `-0.002` n `23`; metal avg `-0.0105` n `18`; unknown avg `0.0268` n `645`
- 1h: commodity avg `0.0933` n `12`; crypto_alt avg `-0.3675` n `228`; crypto_major avg `-0.4865` n `8`; equity avg `-0.1783` n `74`; fx avg `0.0166` n `6`; index avg `0.0184` n `23`; metal avg `0.0233` n `18`; unknown avg `0.0715` n `645`
- 4h: commodity avg `0.3418` n `12`; crypto_alt avg `-0.5316` n `228`; crypto_major avg `-0.2777` n `8`; equity avg `0.0449` n `74`; fx avg `0.0318` n `6`; index avg `0.116` n `23`; metal avg `-0.0505` n `18`; unknown avg `0.368` n `629`
- 24h: commodity avg `-0.2469` n `12`; crypto_alt avg `-0.5217` n `228`; crypto_major avg `0.042` n `8`; equity avg `0.8152` n `74`; fx avg `-0.0124` n `6`; index avg `0.2277` n `23`; metal avg `0.1304` n `18`; unknown avg `-0.9544` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
