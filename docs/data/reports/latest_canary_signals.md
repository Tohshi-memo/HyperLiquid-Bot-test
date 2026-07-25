# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T17:52:25.805863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0742` n `12`; crypto_alt avg `-0.0431` n `230`; crypto_major avg `0.0841` n `8`; equity avg `0.0225` n `100`; fx avg `-0.017` n `6`; index avg `0.0084` n `25`; metal avg `0.006` n `20`; unknown avg `0.0562` n `774`
- 1h: commodity avg `-0.1301` n `12`; crypto_alt avg `0.2358` n `230`; crypto_major avg `0.4312` n `8`; equity avg `0.1465` n `100`; fx avg `-0.0169` n `6`; index avg `0.0596` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.0606` n `774`
- 4h: commodity avg `-0.1053` n `12`; crypto_alt avg `0.6568` n `230`; crypto_major avg `1.1141` n `8`; equity avg `0.2085` n `100`; fx avg `-0.0248` n `6`; index avg `0.0454` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0625` n `774`
- 24h: commodity avg `-0.3807` n `12`; crypto_alt avg `0.2594` n `230`; crypto_major avg `1.1041` n `8`; equity avg `-0.6778` n `100`; fx avg `-0.0208` n `6`; index avg `-0.0377` n `25`; metal avg `-0.0989` n `20`; unknown avg `-0.2957` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1289`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1182`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.112`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
