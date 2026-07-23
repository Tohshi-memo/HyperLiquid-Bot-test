# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T06:22:28.105721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0835` n `230`; crypto_major avg `0.0074` n `8`; equity avg `0.0201` n `98`; fx avg `-0.0196` n `6`; index avg `0.0092` n `25`; metal avg `0.0071` n `20`; unknown avg `0.0273` n `773`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.0531` n `230`; crypto_major avg `-0.0964` n `8`; equity avg `-0.0739` n `98`; fx avg `-0.002` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0276` n `20`; unknown avg `-0.0145` n `741`
- 4h: commodity avg `0.0633` n `12`; crypto_alt avg `0.0608` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `0.1851` n `98`; fx avg `0.0125` n `6`; index avg `0.0413` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.1659` n `741`
- 24h: commodity avg `0.6544` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `0.2031` n `8`; equity avg `0.5865` n `98`; fx avg `-0.1195` n `6`; index avg `0.1828` n `25`; metal avg `-0.112` n `20`; unknown avg `1.6211` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
