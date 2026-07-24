# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T18:52:11.159555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `0.201` n `230`; crypto_major avg `0.2514` n `8`; equity avg `0.1449` n `100`; fx avg `-0.0005` n `6`; index avg `0.006` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0307` n `773`
- 1h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.1175` n `230`; crypto_major avg `-0.0043` n `8`; equity avg `-0.6627` n `100`; fx avg `0.003` n `6`; index avg `-0.1309` n `25`; metal avg `-0.0809` n `20`; unknown avg `-0.0514` n `773`
- 4h: commodity avg `-0.2476` n `12`; crypto_alt avg `0.4126` n `230`; crypto_major avg `0.2901` n `8`; equity avg `-0.1224` n `100`; fx avg `-0.0026` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0091` n `20`; unknown avg `-0.1049` n `773`
- 24h: commodity avg `-0.5742` n `12`; crypto_alt avg `-0.8915` n `230`; crypto_major avg `-0.7873` n `8`; equity avg `-2.8896` n `100`; fx avg `-0.1564` n `6`; index avg `-0.3607` n `25`; metal avg `0.0447` n `20`; unknown avg `14.2011` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1202`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1099`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
