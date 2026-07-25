# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T22:22:29.388921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.0338` n `230`; crypto_major avg `0.0178` n `8`; equity avg `0.0289` n `100`; fx avg `-0.0008` n `6`; index avg `0.004` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0411` n `774`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.2282` n `230`; crypto_major avg `0.1447` n `8`; equity avg `0.0219` n `100`; fx avg `-0.0036` n `6`; index avg `0.0062` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.1249` n `774`
- 4h: commodity avg `0.0764` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.2001` n `8`; equity avg `0.1152` n `100`; fx avg `0.0153` n `6`; index avg `0.0204` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.1708` n `774`
- 24h: commodity avg `-0.5926` n `12`; crypto_alt avg `0.8615` n `230`; crypto_major avg `1.3274` n `8`; equity avg `0.4303` n `100`; fx avg `-0.0001` n `6`; index avg `0.1498` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.3096` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1351`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1227`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
