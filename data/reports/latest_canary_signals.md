# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T05:52:30.262196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.1408` n `230`; crypto_major avg `-0.008` n `8`; equity avg `0.0103` n `100`; fx avg `-0.0005` n `6`; index avg `0.0083` n `25`; metal avg `0.0102` n `20`; unknown avg `2.4663` n `775`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.185` n `230`; crypto_major avg `0.0031` n `8`; equity avg `-0.0728` n `100`; fx avg `-0.0044` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.0829` n `775`
- 4h: commodity avg `-0.0906` n `12`; crypto_alt avg `0.5824` n `230`; crypto_major avg `0.4144` n `8`; equity avg `0.0341` n `100`; fx avg `0.0644` n `6`; index avg `0.0046` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0298` n `774`
- 24h: commodity avg `-0.5367` n `12`; crypto_alt avg `1.3244` n `230`; crypto_major avg `1.7447` n `8`; equity avg `0.46` n `100`; fx avg `0.0681` n `6`; index avg `0.1322` n `25`; metal avg `0.0542` n `20`; unknown avg `-0.1093` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1383`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1232`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1198`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
