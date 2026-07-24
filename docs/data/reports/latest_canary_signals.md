# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T21:33:23.634028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.1235` n `230`; crypto_major avg `0.0847` n `8`; equity avg `0.0688` n `100`; fx avg `0.0059` n `6`; index avg `0.0104` n `25`; metal avg `0.002` n `20`; unknown avg `0.0104` n `774`
- 1h: commodity avg `0.0898` n `12`; crypto_alt avg `-0.1339` n `230`; crypto_major avg `-0.2429` n `8`; equity avg `-0.0066` n `100`; fx avg `-0.0003` n `6`; index avg `0.0218` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0001` n `774`
- 4h: commodity avg `0.3426` n `12`; crypto_alt avg `-0.3419` n `230`; crypto_major avg `-0.366` n `8`; equity avg `-1.0512` n `100`; fx avg `-0.0091` n `6`; index avg `-0.1773` n `25`; metal avg `-0.1595` n `20`; unknown avg `-0.0705` n `773`
- 24h: commodity avg `-0.2547` n `12`; crypto_alt avg `-1.0735` n `230`; crypto_major avg `-1.1141` n `8`; equity avg `-3.2646` n `100`; fx avg `-0.1605` n `6`; index avg `-0.4753` n `25`; metal avg `-0.0367` n `20`; unknown avg `14.0747` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1269`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.122`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
