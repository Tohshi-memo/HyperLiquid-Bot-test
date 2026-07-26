# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T17:37:26.686095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.0575` n `230`; crypto_major avg `-0.0568` n `8`; equity avg `-0.0093` n `100`; fx avg `0.0092` n `6`; index avg `0.0062` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0275` n `775`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `-0.2371` n `230`; crypto_major avg `-0.2579` n `8`; equity avg `-0.0366` n `100`; fx avg `0.0062` n `6`; index avg `0.0021` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.0454` n `775`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `0.3862` n `230`; crypto_major avg `0.552` n `8`; equity avg `0.1363` n `100`; fx avg `-0.0076` n `6`; index avg `0.0365` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.1156` n `775`
- 24h: commodity avg `-0.394` n `12`; crypto_alt avg `0.8213` n `230`; crypto_major avg `0.8142` n `8`; equity avg `0.7539` n `100`; fx avg `0.0213` n `6`; index avg `0.1617` n `25`; metal avg `0.174` n `20`; unknown avg `-0.0498` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
