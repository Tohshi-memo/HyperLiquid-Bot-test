# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T23:43:55.821462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `-0.0702` n `230`; crypto_major avg `-0.1298` n `8`; equity avg `-0.1316` n `100`; fx avg `-0.0087` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.1403` n `772`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `-0.0755` n `230`; crypto_major avg `-0.0295` n `8`; equity avg `-0.0535` n `100`; fx avg `-0.0032` n `6`; index avg `0.0353` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.1517` n `772`
- 4h: commodity avg `0.0683` n `12`; crypto_alt avg `-0.1495` n `230`; crypto_major avg `0.0478` n `8`; equity avg `0.009` n `100`; fx avg `-0.0195` n `6`; index avg `0.0517` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0509` n `772`
- 24h: commodity avg `0.6829` n `12`; crypto_alt avg `-1.4667` n `230`; crypto_major avg `-1.9997` n `8`; equity avg `-1.2478` n `99`; fx avg `-0.0788` n `6`; index avg `-0.2403` n `25`; metal avg `-0.6997` n `20`; unknown avg `-0.2635` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
