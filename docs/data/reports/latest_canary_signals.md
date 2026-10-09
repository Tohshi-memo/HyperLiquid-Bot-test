# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T12:37:33.148780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `-0.1341` n `235`; crypto_major avg `-0.0837` n `8`; equity avg `-0.0827` n `150`; fx avg `-0.0032` n `6`; index avg `-0.0247` n `26`; metal avg `-0.0198` n `20`; unknown avg `0.2284` n `1078`
- 1h: commodity avg `0.0568` n `13`; crypto_alt avg `-0.1869` n `235`; crypto_major avg `0.0546` n `8`; equity avg `-0.1162` n `150`; fx avg `-0.0336` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0555` n `20`; unknown avg `1.4355` n `1070`
- 4h: commodity avg `0.1057` n `13`; crypto_alt avg `-0.454` n `235`; crypto_major avg `0.091` n `8`; equity avg `-0.1281` n `150`; fx avg `-0.0899` n `6`; index avg `-0.0524` n `26`; metal avg `-0.08` n `20`; unknown avg `1.8649` n `1070`
- 24h: commodity avg `-0.4643` n `13`; crypto_alt avg `-0.9518` n `235`; crypto_major avg `-0.7173` n `8`; equity avg `-0.243` n `150`; fx avg `0.0107` n `6`; index avg `0.0427` n `26`; metal avg `0.5188` n `20`; unknown avg `7.4893` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
