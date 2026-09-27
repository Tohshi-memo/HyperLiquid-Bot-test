# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T16:52:27.602324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2278` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0271` n `234`; crypto_major avg `0.0138` n `8`; equity avg `0.0` n `141`; fx avg `0.0003` n `6`; index avg `-0.0126` n `26`; metal avg `-0.003` n `20`; unknown avg `0.4897` n `962`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `0.3735` n `234`; crypto_major avg `0.0504` n `8`; equity avg `0.036` n `141`; fx avg `0.0095` n `6`; index avg `-0.0109` n `26`; metal avg `0.0042` n `20`; unknown avg `0.1764` n `954`
- 4h: commodity avg `-0.169` n `12`; crypto_alt avg `-0.8791` n `234`; crypto_major avg `-1.2419` n `8`; equity avg `-0.0685` n `141`; fx avg `0.0133` n `6`; index avg `-0.0141` n `26`; metal avg `0.0008` n `20`; unknown avg `5.9439` n `954`
- 24h: commodity avg `-0.1313` n `12`; crypto_alt avg `-1.1544` n `234`; crypto_major avg `-0.5219` n `8`; equity avg `0.1896` n `141`; fx avg `-0.0095` n `6`; index avg `0.0002` n `26`; metal avg `-0.0119` n `20`; unknown avg `125.2006` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
