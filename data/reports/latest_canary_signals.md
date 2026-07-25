# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T10:22:27.638958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.0445` n `230`; crypto_major avg `0.0047` n `8`; equity avg `0.0008` n `100`; fx avg `0.001` n `6`; index avg `-0.0006` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.0045` n `774`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.1656` n `230`; crypto_major avg `0.2075` n `8`; equity avg `0.014` n `100`; fx avg `-0.0142` n `6`; index avg `0.0015` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.0024` n `774`
- 4h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.1269` n `230`; crypto_major avg `0.1072` n `8`; equity avg `-0.0918` n `100`; fx avg `0.0184` n `6`; index avg `0.0011` n `25`; metal avg `0.002` n `20`; unknown avg `-0.2033` n `774`
- 24h: commodity avg `0.0061` n `12`; crypto_alt avg `-1.4003` n `230`; crypto_major avg `-1.0461` n `8`; equity avg `-3.0044` n `100`; fx avg `-0.007` n `6`; index avg `-0.274` n `25`; metal avg `-0.1554` n `20`; unknown avg `13.1674` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1173`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1013`, n `666`, weak_sample_signal
