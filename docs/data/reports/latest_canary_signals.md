# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T12:37:23.323105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.004` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0208` n `100`; fx avg `-0.0025` n `6`; index avg `-0.0043` n `25`; metal avg `0.0024` n `20`; unknown avg `0.015` n `774`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.0395` n `230`; crypto_major avg `-0.0735` n `8`; equity avg `0.0158` n `100`; fx avg `-0.0019` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0081` n `774`
- 4h: commodity avg `-0.0671` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `0.1349` n `8`; equity avg `-0.0009` n `100`; fx avg `-0.0174` n `6`; index avg `0.0163` n `25`; metal avg `0.0032` n `20`; unknown avg `0.302` n `774`
- 24h: commodity avg `-0.1376` n `12`; crypto_alt avg `-1.328` n `230`; crypto_major avg `-0.9987` n `8`; equity avg `-2.9859` n `100`; fx avg `-0.0083` n `6`; index avg `-0.2997` n `25`; metal avg `-0.1731` n `20`; unknown avg `13.1697` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1187`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1025`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
