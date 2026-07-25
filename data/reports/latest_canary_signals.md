# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T03:52:30.470617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.1429` n `230`; crypto_major avg `-0.0745` n `8`; equity avg `0.0002` n `100`; fx avg `0.0014` n `6`; index avg `-0.0052` n `25`; metal avg `-0.002` n `20`; unknown avg `0.0335` n `774`
- 1h: commodity avg `-0.0462` n `12`; crypto_alt avg `0.0111` n `230`; crypto_major avg `0.0627` n `8`; equity avg `0.0727` n `100`; fx avg `0.0007` n `6`; index avg `0.0028` n `25`; metal avg `-0.0083` n `20`; unknown avg `4.5682` n `774`
- 4h: commodity avg `-0.169` n `12`; crypto_alt avg `-0.0397` n `230`; crypto_major avg `-0.0165` n `8`; equity avg `0.3358` n `100`; fx avg `-0.0318` n `6`; index avg `0.0679` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.884` n `774`
- 24h: commodity avg `-0.5162` n `12`; crypto_alt avg `-1.2833` n `230`; crypto_major avg `-1.1619` n `8`; equity avg `-2.2264` n `100`; fx avg `-0.0535` n `6`; index avg `-0.144` n `25`; metal avg `0.1468` n `20`; unknown avg `13.8371` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1157`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.108`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1004`, n `666`, weak_sample_signal
