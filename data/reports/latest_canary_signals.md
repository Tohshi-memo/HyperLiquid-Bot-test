# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T09:22:36.938348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `0.0246` n `234`; crypto_major avg `0.0979` n `8`; equity avg `0.0069` n `142`; fx avg `-0.0078` n `6`; index avg `0.0026` n `26`; metal avg `-0.0493` n `20`; unknown avg `3.3271` n `963`
- 1h: commodity avg `0.1757` n `12`; crypto_alt avg `0.3844` n `234`; crypto_major avg `0.2739` n `8`; equity avg `-0.1041` n `142`; fx avg `0.0259` n `6`; index avg `-0.0292` n `26`; metal avg `-0.1546` n `20`; unknown avg `3.5853` n `961`
- 4h: commodity avg `0.1431` n `12`; crypto_alt avg `0.5832` n `234`; crypto_major avg `0.232` n `8`; equity avg `0.1219` n `142`; fx avg `0.0519` n `6`; index avg `0.0327` n `26`; metal avg `0.079` n `20`; unknown avg `4.0798` n `915`
- 24h: commodity avg `-0.4029` n `12`; crypto_alt avg `0.3704` n `234`; crypto_major avg `-0.6487` n `8`; equity avg `0.2952` n `142`; fx avg `-0.015` n `6`; index avg `0.0817` n `26`; metal avg `0.193` n `20`; unknown avg `2920.7464` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
