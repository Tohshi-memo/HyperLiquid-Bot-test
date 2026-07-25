# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T14:07:34.548625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0286` n `230`; crypto_major avg `-0.0649` n `8`; equity avg `-0.0094` n `100`; fx avg `0.0023` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0215` n `774`
- 1h: commodity avg `-0.3605` n `12`; crypto_alt avg `-0.0625` n `230`; crypto_major avg `-0.0715` n `8`; equity avg `-0.0374` n `100`; fx avg `0.0024` n `6`; index avg `0.0008` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0311` n `774`
- 4h: commodity avg `-0.4176` n `12`; crypto_alt avg `0.2479` n `230`; crypto_major avg `0.1123` n `8`; equity avg `-0.0277` n `100`; fx avg `-0.0068` n `6`; index avg `0.0031` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0194` n `774`
- 24h: commodity avg `-0.5339` n `12`; crypto_alt avg `-0.0437` n `230`; crypto_major avg `0.2229` n `8`; equity avg `-0.9213` n `100`; fx avg `-0.0085` n `6`; index avg `-0.0239` n `25`; metal avg `0.0175` n `20`; unknown avg `13.2644` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.124`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1078`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
