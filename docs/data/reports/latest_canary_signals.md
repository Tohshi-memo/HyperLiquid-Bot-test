# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T14:22:31.765642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0219` n `230`; crypto_major avg `-0.014` n `8`; equity avg `0.0116` n `100`; fx avg `-0.0073` n `6`; index avg `0.0041` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0209` n `774`
- 1h: commodity avg `-0.3626` n `12`; crypto_alt avg `-0.0738` n `230`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0086` n `100`; fx avg `-0.0098` n `6`; index avg `0.0115` n `25`; metal avg `0.0139` n `20`; unknown avg `0.1053` n `774`
- 4h: commodity avg `-0.415` n `12`; crypto_alt avg `0.1813` n `230`; crypto_major avg `0.0936` n `8`; equity avg `-0.0162` n `100`; fx avg `-0.0151` n `6`; index avg `0.0078` n `25`; metal avg `0.0168` n `20`; unknown avg `0.0124` n `774`
- 24h: commodity avg `-0.5412` n `12`; crypto_alt avg `0.175` n `230`; crypto_major avg `0.5326` n `8`; equity avg `-0.7471` n `100`; fx avg `-0.0199` n `6`; index avg `-0.021` n `25`; metal avg `-0.0072` n `20`; unknown avg `13.3122` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1236`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1075`, n `666`, weak_sample_signal
