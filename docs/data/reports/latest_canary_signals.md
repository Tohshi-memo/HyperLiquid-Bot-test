# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T13:37:25.330156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0642` n `230`; crypto_major avg `-0.0824` n `8`; equity avg `0.0048` n `100`; fx avg `-0.0044` n `6`; index avg `-0.0027` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0048` n `775`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `-0.2612` n `230`; crypto_major avg `-0.1926` n `8`; equity avg `0.0287` n `100`; fx avg `-0.0038` n `6`; index avg `-0.0051` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0373` n `775`
- 4h: commodity avg `-0.1751` n `12`; crypto_alt avg `-0.1562` n `230`; crypto_major avg `-0.1266` n `8`; equity avg `0.2127` n `100`; fx avg `0.0047` n `6`; index avg `0.036` n `25`; metal avg `0.0903` n `20`; unknown avg `-0.0967` n `775`
- 24h: commodity avg `-0.7589` n `12`; crypto_alt avg `1.1084` n `230`; crypto_major avg `1.2713` n `8`; equity avg `0.7842` n `100`; fx avg `0.0173` n `6`; index avg `0.1727` n `25`; metal avg `0.1956` n `20`; unknown avg `0.0381` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
