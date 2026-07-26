# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T09:52:29.019120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `-0.0371` n `230`; crypto_major avg `0.0313` n `8`; equity avg `0.0062` n `100`; fx avg `-0.0005` n `6`; index avg `0.0001` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.0288` n `775`
- 1h: commodity avg `-0.1004` n `12`; crypto_alt avg `-0.0584` n `230`; crypto_major avg `0.0584` n `8`; equity avg `0.0521` n `100`; fx avg `0.0017` n `6`; index avg `0.013` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.0317` n `775`
- 4h: commodity avg `-0.1501` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `0.0133` n `8`; equity avg `0.0506` n `100`; fx avg `-0.0384` n `6`; index avg `0.0169` n `25`; metal avg `0.0722` n `20`; unknown avg `-0.0542` n `759`
- 24h: commodity avg `-0.7417` n `12`; crypto_alt avg `1.4148` n `230`; crypto_major avg `1.5384` n `8`; equity avg `0.5993` n `100`; fx avg `0.0101` n `6`; index avg `0.1331` n `25`; metal avg `0.108` n `20`; unknown avg `0.0248` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1456`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.132`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1305`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
