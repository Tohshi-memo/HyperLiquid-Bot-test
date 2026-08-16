# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T13:37:26.434858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `-0.0095` n `230`; crypto_major avg `-0.03` n `8`; equity avg `-0.0008` n `114`; fx avg `-0.0012` n `6`; index avg `0.0052` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0465` n `791`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0663` n `230`; crypto_major avg `0.0491` n `8`; equity avg `-0.0152` n `114`; fx avg `-0.0103` n `6`; index avg `0.0076` n `25`; metal avg `-0.0139` n `20`; unknown avg `0.0406` n `791`
- 4h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0344` n `230`; crypto_major avg `-0.0574` n `8`; equity avg `-0.1216` n `114`; fx avg `-0.0203` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.14` n `791`
- 24h: commodity avg `0.0395` n `12`; crypto_alt avg `0.0624` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.2483` n `114`; fx avg `-0.0151` n `6`; index avg `0.0388` n `25`; metal avg `0.0251` n `20`; unknown avg `0.1039` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
