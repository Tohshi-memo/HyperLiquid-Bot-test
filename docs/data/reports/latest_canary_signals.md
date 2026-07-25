# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T19:37:26.287563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.0355` n `230`; crypto_major avg `-0.0691` n `8`; equity avg `0.0097` n `100`; fx avg `0.0078` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0054` n `774`
- 1h: commodity avg `-0.1352` n `12`; crypto_alt avg `-0.1013` n `230`; crypto_major avg `-0.1287` n `8`; equity avg `0.0269` n `100`; fx avg `0.0288` n `6`; index avg `-0.0063` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0295` n `774`
- 4h: commodity avg `-0.0639` n `12`; crypto_alt avg `0.3055` n `230`; crypto_major avg `0.5713` n `8`; equity avg `0.2078` n `100`; fx avg `-0.0017` n `6`; index avg `0.0396` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.1238` n `774`
- 24h: commodity avg `-0.3799` n `12`; crypto_alt avg `0.3814` n `230`; crypto_major avg `0.9489` n `8`; equity avg `0.285` n `100`; fx avg `-0.0024` n `6`; index avg `0.1004` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.3036` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1319`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1181`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1141`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1113`, n `666`, weak_sample_signal
