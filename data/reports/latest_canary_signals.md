# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T04:52:32.535751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0703` n `230`; crypto_major avg `0.0352` n `8`; equity avg `0.0205` n `100`; fx avg `0.0` n `6`; index avg `0.0003` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0332` n `775`
- 1h: commodity avg `-0.0536` n `12`; crypto_alt avg `0.1544` n `230`; crypto_major avg `0.1534` n `8`; equity avg `0.0469` n `100`; fx avg `0.0642` n `6`; index avg `0.0013` n `25`; metal avg `0.014` n `20`; unknown avg `-0.0836` n `775`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `0.4969` n `230`; crypto_major avg `0.5107` n `8`; equity avg `0.2622` n `100`; fx avg `0.0709` n `6`; index avg `0.0484` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0931` n `774`
- 24h: commodity avg `-0.526` n `12`; crypto_alt avg `0.8973` n `230`; crypto_major avg `1.494` n `8`; equity avg `0.4758` n `100`; fx avg `0.0654` n `6`; index avg `0.1328` n `25`; metal avg `0.0583` n `20`; unknown avg `-0.1834` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1241`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1181`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
