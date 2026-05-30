# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T10:07:20.218179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0482` n `228`; crypto_major avg `-0.0234` n `8`; equity avg `0.0115` n `69`; fx avg `0.0013` n `6`; index avg `-0.0051` n `23`; metal avg `0.0018` n `18`; unknown avg `-0.0553` n `421`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `0.1034` n `228`; crypto_major avg `0.1273` n `8`; equity avg `0.0081` n `69`; fx avg `0.0019` n `6`; index avg `-0.021` n `23`; metal avg `0.035` n `18`; unknown avg `0.0603` n `421`
- 4h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0511` n `228`; crypto_major avg `0.2226` n `8`; equity avg `0.1125` n `69`; fx avg `0.0232` n `6`; index avg `-0.0345` n `23`; metal avg `0.0201` n `18`; unknown avg `-0.3948` n `421`
- 24h: commodity avg `-0.2841` n `12`; crypto_alt avg `1.1253` n `228`; crypto_major avg `1.7534` n `8`; equity avg `1.1712` n `69`; fx avg `0.103` n `6`; index avg `0.1081` n `23`; metal avg `-0.0527` n `18`; unknown avg `0.4008` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
