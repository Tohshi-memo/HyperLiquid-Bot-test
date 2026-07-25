# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T03:37:29.866907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `0.0869` n `230`; crypto_major avg `0.036` n `8`; equity avg `-0.0057` n `100`; fx avg `0.0015` n `6`; index avg `0.0008` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.0041` n `774`
- 1h: commodity avg `-0.0831` n `12`; crypto_alt avg `0.114` n `230`; crypto_major avg `0.0791` n `8`; equity avg `0.1353` n `100`; fx avg `0.0013` n `6`; index avg `0.0311` n `25`; metal avg `-0.0059` n `20`; unknown avg `1.5053` n `774`
- 4h: commodity avg `-0.168` n `12`; crypto_alt avg `0.1453` n `230`; crypto_major avg `0.1301` n `8`; equity avg `0.3566` n `100`; fx avg `-0.0373` n `6`; index avg `0.079` n `25`; metal avg `-0.0285` n `20`; unknown avg `0.2979` n `774`
- 24h: commodity avg `-0.5258` n `12`; crypto_alt avg `-1.146` n `230`; crypto_major avg `-1.0394` n `8`; equity avg `-2.2241` n `100`; fx avg `-0.059` n `6`; index avg `-0.1418` n `25`; metal avg `0.1699` n `20`; unknown avg `13.9682` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1163`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1085`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1032`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1011`, n `666`, weak_sample_signal
