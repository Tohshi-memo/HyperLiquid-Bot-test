# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T07:37:17.517590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `-0.1458` n `228`; crypto_major avg `-0.0417` n `8`; equity avg `-0.03` n `65`; fx avg `0.0` n `5`; index avg `0.0083` n `23`; metal avg `0.0102` n `18`; unknown avg `0.2586` n `376`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `-0.2752` n `228`; crypto_major avg `-0.009` n `8`; equity avg `-0.0356` n `65`; fx avg `0.0011` n `5`; index avg `0.0399` n `23`; metal avg `0.0111` n `18`; unknown avg `0.2481` n `376`
- 4h: commodity avg `0.1543` n `12`; crypto_alt avg `-0.3219` n `228`; crypto_major avg `-0.1533` n `8`; equity avg `-0.0158` n `65`; fx avg `0.0191` n `5`; index avg `0.0899` n `23`; metal avg `-0.0183` n `18`; unknown avg `-0.0139` n `355`
- 24h: commodity avg `-0.0108` n `12`; crypto_alt avg `4.2258` n `228`; crypto_major avg `2.7144` n `8`; equity avg `3.2548` n `65`; fx avg `0.0084` n `5`; index avg `1.3507` n `23`; metal avg `0.1649` n `18`; unknown avg `1.4507` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
