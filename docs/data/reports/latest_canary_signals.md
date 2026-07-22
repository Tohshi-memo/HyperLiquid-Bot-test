# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T07:07:28.562288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0622` n `12`; crypto_alt avg `-0.0807` n `230`; crypto_major avg `-0.0221` n `8`; equity avg `-0.1135` n `98`; fx avg `0.0062` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0165` n `20`; unknown avg `-0.035` n `772`
- 1h: commodity avg `0.2314` n `12`; crypto_alt avg `-0.2013` n `230`; crypto_major avg `-0.1216` n `8`; equity avg `-0.1102` n `98`; fx avg `-0.0223` n `6`; index avg `-0.0619` n `25`; metal avg `-0.1587` n `20`; unknown avg `-0.0097` n `772`
- 4h: commodity avg `0.2029` n `12`; crypto_alt avg `-1.0127` n `230`; crypto_major avg `-1.1307` n `8`; equity avg `-1.1778` n `98`; fx avg `-0.05` n `6`; index avg `-0.2805` n `25`; metal avg `-0.257` n `20`; unknown avg `-0.2393` n `739`
- 24h: commodity avg `0.6978` n `12`; crypto_alt avg `-1.286` n `230`; crypto_major avg `-1.578` n `8`; equity avg `0.6432` n `98`; fx avg `-0.0094` n `6`; index avg `-0.0036` n `25`; metal avg `0.2306` n `20`; unknown avg `0.0209` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1003`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0837`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.071`, n `666`, weak_sample_signal
