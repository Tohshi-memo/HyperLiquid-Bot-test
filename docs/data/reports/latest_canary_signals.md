# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T21:37:28.903420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1862` n `230`; crypto_major avg `0.0946` n `8`; equity avg `0.0124` n `100`; fx avg `-0.0012` n `6`; index avg `0.0019` n `25`; metal avg `0.025` n `20`; unknown avg `0.0094` n `775`
- 1h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.2265` n `230`; crypto_major avg `0.2341` n `8`; equity avg `0.0939` n `100`; fx avg `-0.0057` n `6`; index avg `0.0034` n `25`; metal avg `0.0729` n `20`; unknown avg `-0.0222` n `775`
- 4h: commodity avg `0.1462` n `12`; crypto_alt avg `0.035` n `230`; crypto_major avg `0.1026` n `8`; equity avg `0.0399` n `100`; fx avg `0.036` n `6`; index avg `-0.0449` n `25`; metal avg `0.0762` n `20`; unknown avg `-0.3468` n `775`
- 24h: commodity avg `-0.3119` n `12`; crypto_alt avg `0.9129` n `230`; crypto_major avg `0.9953` n `8`; equity avg `0.6699` n `100`; fx avg `0.0458` n `6`; index avg `0.0926` n `25`; metal avg `0.2452` n `20`; unknown avg `-0.0851` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
