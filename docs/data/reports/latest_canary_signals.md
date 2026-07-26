# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T18:22:27.756430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `-0.0106` n `230`; crypto_major avg `0.0601` n `8`; equity avg `-0.0174` n `100`; fx avg `0.0008` n `6`; index avg `0.0001` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0469` n `775`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `-0.1545` n `230`; crypto_major avg `-0.077` n `8`; equity avg `-0.015` n `100`; fx avg `0.0156` n `6`; index avg `0.0027` n `25`; metal avg `0.0124` n `20`; unknown avg `0.5868` n `775`
- 4h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.2214` n `230`; crypto_major avg `0.3134` n `8`; equity avg `0.0816` n `100`; fx avg `-0.0026` n `6`; index avg `0.018` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.1102` n `775`
- 24h: commodity avg `-0.3202` n `12`; crypto_alt avg `0.6902` n `230`; crypto_major avg `0.7314` n `8`; equity avg `0.7201` n `100`; fx avg `0.0433` n `6`; index avg `0.1521` n `25`; metal avg `0.1888` n `20`; unknown avg `-0.0527` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1936`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1652`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1396`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1324`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1304`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `669`, weak_sample_signal
