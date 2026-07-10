# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T04:52:29.632018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0518` n `12`; crypto_alt avg `0.0296` n `229`; crypto_major avg `0.0188` n `8`; equity avg `-0.0631` n `91`; fx avg `-0.0017` n `6`; index avg `-0.0265` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0454` n `765`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.0026` n `229`; crypto_major avg `0.0915` n `8`; equity avg `0.0036` n `91`; fx avg `0.0215` n `6`; index avg `-0.0122` n `25`; metal avg `-0.0233` n `20`; unknown avg `-0.1841` n `765`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `1.0894` n `229`; crypto_major avg `1.5369` n `8`; equity avg `0.3362` n `91`; fx avg `0.0026` n `6`; index avg `0.1008` n `25`; metal avg `0.172` n `20`; unknown avg `3.1581` n `763`
- 24h: commodity avg `-1.0597` n `12`; crypto_alt avg `1.3562` n `229`; crypto_major avg `1.6173` n `8`; equity avg `1.6443` n `91`; fx avg `0.0751` n `6`; index avg `0.4111` n `25`; metal avg `0.9132` n `20`; unknown avg `0.167` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
