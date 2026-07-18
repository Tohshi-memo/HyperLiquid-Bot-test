# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T14:07:28.929230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `0.0304` n `8`; equity avg `-0.0675` n `96`; fx avg `0.0` n `6`; index avg `0.0023` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.0011` n `770`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.1683` n `230`; crypto_major avg `-0.0809` n `8`; equity avg `-0.034` n `96`; fx avg `0.0013` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0405` n `770`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `-0.314` n `230`; crypto_major avg `-0.0807` n `8`; equity avg `-0.1143` n `96`; fx avg `-0.0046` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0184` n `20`; unknown avg `-0.0608` n `769`
- 24h: commodity avg `0.3917` n `12`; crypto_alt avg `-0.9339` n `230`; crypto_major avg `-0.0048` n `8`; equity avg `-0.2066` n `96`; fx avg `0.0172` n `6`; index avg `0.0709` n `25`; metal avg `0.1995` n `20`; unknown avg `-0.008` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
