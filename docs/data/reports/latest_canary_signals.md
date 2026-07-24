# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T15:07:28.829877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0659` n `12`; crypto_alt avg `-0.0082` n `230`; crypto_major avg `-0.0413` n `8`; equity avg `0.3725` n `100`; fx avg `0.0164` n `6`; index avg `0.0492` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0777` n `773`
- 1h: commodity avg `0.1008` n `12`; crypto_alt avg `-0.1274` n `230`; crypto_major avg `-0.0337` n `8`; equity avg `-0.2091` n `100`; fx avg `0.0071` n `6`; index avg `0.0198` n `25`; metal avg `0.0839` n `20`; unknown avg `13.3112` n `773`
- 4h: commodity avg `0.1766` n `12`; crypto_alt avg `-1.2362` n `230`; crypto_major avg `-1.2128` n `8`; equity avg `-2.2755` n `100`; fx avg `0.003` n `6`; index avg `-0.2202` n `25`; metal avg `-0.0813` n `20`; unknown avg `13.2196` n `773`
- 24h: commodity avg `-0.2633` n `12`; crypto_alt avg `-1.8452` n `230`; crypto_major avg `-1.5788` n `8`; equity avg `-2.2006` n `100`; fx avg `-0.1303` n `6`; index avg `-0.2598` n `25`; metal avg `-0.0219` n `20`; unknown avg `13.8639` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1245`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1218`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1056`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1041`, n `666`, weak_sample_signal
