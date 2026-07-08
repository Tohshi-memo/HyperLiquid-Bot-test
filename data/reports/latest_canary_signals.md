# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T05:52:29.500051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.1833` n `229`; crypto_major avg `-0.1131` n `8`; equity avg `0.0375` n `91`; fx avg `0.009` n `6`; index avg `0.0076` n `25`; metal avg `-0.05` n `20`; unknown avg `4.4541` n `761`
- 1h: commodity avg `0.0989` n `12`; crypto_alt avg `0.0865` n `229`; crypto_major avg `-0.0588` n `8`; equity avg `-0.0834` n `91`; fx avg `-0.0253` n `6`; index avg `-0.0409` n `25`; metal avg `0.0477` n `20`; unknown avg `0.5548` n `761`
- 4h: commodity avg `0.1668` n `12`; crypto_alt avg `-0.417` n `229`; crypto_major avg `-0.7452` n `8`; equity avg `-0.2646` n `91`; fx avg `-0.0409` n `6`; index avg `-0.2576` n `25`; metal avg `0.3032` n `20`; unknown avg `-0.083` n `761`
- 24h: commodity avg `0.9581` n `12`; crypto_alt avg `-2.6415` n `229`; crypto_major avg `-2.1708` n `8`; equity avg `-1.6629` n `91`; fx avg `-0.2163` n `6`; index avg `-0.3349` n `25`; metal avg `0.1893` n `20`; unknown avg `-0.3994` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
