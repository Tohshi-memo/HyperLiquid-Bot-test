# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T18:52:28.484884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0392` n `12`; crypto_alt avg `-0.0248` n `230`; crypto_major avg `0.0308` n `8`; equity avg `0.0087` n `100`; fx avg `0.0` n `6`; index avg `0.0008` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.047` n `774`
- 1h: commodity avg `0.1253` n `12`; crypto_alt avg `-0.0068` n `230`; crypto_major avg `0.0471` n `8`; equity avg `0.0336` n `100`; fx avg `-0.0036` n `6`; index avg `-0.0001` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.1326` n `774`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.6537` n `230`; crypto_major avg `1.0506` n `8`; equity avg `0.1865` n `100`; fx avg `-0.0292` n `6`; index avg `0.0555` n `25`; metal avg `0.0048` n `20`; unknown avg `0.2469` n `774`
- 24h: commodity avg `-0.3158` n `12`; crypto_alt avg `0.3646` n `230`; crypto_major avg `1.1493` n `8`; equity avg `0.0247` n `100`; fx avg `-0.0274` n `6`; index avg `0.0937` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.3324` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1302`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.119`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1129`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1126`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
