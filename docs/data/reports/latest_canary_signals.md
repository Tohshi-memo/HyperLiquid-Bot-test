# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T19:52:27.817650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.058` n `12`; crypto_alt avg `-0.064` n `230`; crypto_major avg `-0.1616` n `8`; equity avg `-0.2512` n `100`; fx avg `0.0019` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.0704` n `773`
- 1h: commodity avg `0.0267` n `12`; crypto_alt avg `-0.1563` n `230`; crypto_major avg `-0.1237` n `8`; equity avg `-0.4936` n `100`; fx avg `0.0057` n `6`; index avg `-0.0534` n `25`; metal avg `-0.038` n `20`; unknown avg `-0.1272` n `773`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.0644` n `230`; crypto_major avg `-0.0867` n `8`; equity avg `-1.4838` n `100`; fx avg `-0.039` n `6`; index avg `-0.2715` n `25`; metal avg `-0.2285` n `20`; unknown avg `-0.0917` n `773`
- 24h: commodity avg `-0.4493` n `12`; crypto_alt avg `-0.7309` n `230`; crypto_major avg `-0.4955` n `8`; equity avg `-3.0184` n `100`; fx avg `-0.1612` n `6`; index avg `-0.396` n `25`; metal avg `0.0077` n `20`; unknown avg `13.9143` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1319`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.126`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1135`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
