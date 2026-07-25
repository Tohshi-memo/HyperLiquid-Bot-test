# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T14:52:32.944042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.0173` n `230`; crypto_major avg `0.0618` n `8`; equity avg `0.0195` n `100`; fx avg `-0.0003` n `6`; index avg `-0.0124` n `25`; metal avg `0.0128` n `20`; unknown avg `0.0138` n `774`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `-0.0091` n `230`; crypto_major avg `0.1044` n `8`; equity avg `0.0568` n `100`; fx avg `0.0007` n `6`; index avg `-0.0101` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.1243` n `774`
- 4h: commodity avg `-0.3923` n `12`; crypto_alt avg `0.2228` n `230`; crypto_major avg `0.2952` n `8`; equity avg `0.026` n `100`; fx avg `-0.0087` n `6`; index avg `-0.0055` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.1015` n `774`
- 24h: commodity avg `-0.545` n `12`; crypto_alt avg `0.0984` n `230`; crypto_major avg `0.3875` n `8`; equity avg `-0.2861` n `100`; fx avg `-0.0007` n `6`; index avg `0.0017` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.5065` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.124`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
