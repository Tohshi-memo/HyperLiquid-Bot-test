# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T05:22:32.960694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.0891` n `232`; crypto_major avg `0.1325` n `8`; equity avg `0.1828` n `134`; fx avg `0.0074` n `6`; index avg `0.0332` n `26`; metal avg `-0.0141` n `20`; unknown avg `0.4213` n `797`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `0.3219` n `232`; crypto_major avg `0.1701` n `8`; equity avg `-0.1485` n `134`; fx avg `-0.0064` n `6`; index avg `-0.0454` n `26`; metal avg `-0.0483` n `20`; unknown avg `1.4963` n `773`
- 4h: commodity avg `0.1118` n `12`; crypto_alt avg `-0.4238` n `232`; crypto_major avg `-0.604` n `8`; equity avg `0.1423` n `134`; fx avg `-0.007` n `6`; index avg `0.0321` n `26`; metal avg `-0.0209` n `20`; unknown avg `0.2812` n `767`
- 24h: commodity avg `0.1329` n `12`; crypto_alt avg `0.4798` n `232`; crypto_major avg `-1.1618` n `8`; equity avg `0.5579` n `134`; fx avg `-0.2849` n `6`; index avg `0.1579` n `26`; metal avg `0.3504` n `20`; unknown avg `7463.6219` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
