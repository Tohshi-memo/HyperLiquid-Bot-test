# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T02:37:30.514977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.2938` n `229`; crypto_major avg `-0.2833` n `8`; equity avg `-0.1545` n `91`; fx avg `-0.0008` n `6`; index avg `-0.0305` n `25`; metal avg `0.0441` n `20`; unknown avg `0.1386` n `763`
- 1h: commodity avg `0.0616` n `12`; crypto_alt avg `-0.2209` n `229`; crypto_major avg `-0.48` n `8`; equity avg `0.0417` n `91`; fx avg `-0.0127` n `6`; index avg `-0.0179` n `25`; metal avg `0.1193` n `20`; unknown avg `0.4273` n `761`
- 4h: commodity avg `0.091` n `12`; crypto_alt avg `-1.0856` n `229`; crypto_major avg `-1.1418` n `8`; equity avg `-1.3471` n `91`; fx avg `-0.0584` n `6`; index avg `-0.3951` n `25`; metal avg `-0.1758` n `20`; unknown avg `1.334` n `761`
- 24h: commodity avg `0.2841` n `12`; crypto_alt avg `-0.2143` n `229`; crypto_major avg `-0.8595` n `8`; equity avg `-0.7269` n `90`; fx avg `0.0206` n `6`; index avg `-0.1458` n `25`; metal avg `-0.1639` n `20`; unknown avg `-0.1552` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
