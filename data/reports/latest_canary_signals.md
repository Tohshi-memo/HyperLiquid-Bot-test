# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T08:37:30.088726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0638` n `230`; crypto_major avg `-0.0416` n `8`; equity avg `-0.021` n `100`; fx avg `-0.0052` n `6`; index avg `0.0051` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0174` n `774`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1022` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `-0.0342` n `100`; fx avg `-0.0028` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0305` n `774`
- 4h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.4866` n `230`; crypto_major avg `-0.3293` n `8`; equity avg `-0.1068` n `100`; fx avg `0.0232` n `6`; index avg `-0.0061` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.2505` n `758`
- 24h: commodity avg `-0.0096` n `12`; crypto_alt avg `-1.9317` n `230`; crypto_major avg `-1.7541` n `8`; equity avg `-2.8618` n `100`; fx avg `-0.0348` n `6`; index avg `-0.2551` n `25`; metal avg `-0.0473` n `20`; unknown avg `13.4085` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1146`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
