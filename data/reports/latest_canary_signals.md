# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T02:07:23.577903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.2323` n `228`; crypto_major avg `-0.0193` n `8`; equity avg `-0.0182` n `67`; fx avg `-0.0167` n `6`; index avg `0.0109` n `23`; metal avg `-0.1898` n `18`; unknown avg `-0.0398` n `419`
- 1h: commodity avg `-0.0495` n `12`; crypto_alt avg `-0.3929` n `228`; crypto_major avg `-0.2897` n `8`; equity avg `-0.2077` n `67`; fx avg `0.0009` n `6`; index avg `-0.0546` n `23`; metal avg `-0.8994` n `18`; unknown avg `-0.2588` n `419`
- 4h: commodity avg `0.2631` n `12`; crypto_alt avg `-0.7296` n `228`; crypto_major avg `-0.8786` n `8`; equity avg `-0.3908` n `67`; fx avg `0.011` n `6`; index avg `-0.1995` n `23`; metal avg `-1.2177` n `18`; unknown avg `-0.0644` n `419`
- 24h: commodity avg `-0.5849` n `12`; crypto_alt avg `-2.1845` n `228`; crypto_major avg `-1.7332` n `8`; equity avg `-0.7942` n `67`; fx avg `-0.0681` n `6`; index avg `-0.7463` n `23`; metal avg `-2.1804` n `18`; unknown avg `-0.8776` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
