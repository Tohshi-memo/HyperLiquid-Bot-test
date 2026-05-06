# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T14:37:28.572992+00:00`
- Correlation status: `ready`
- Asset price records: `462`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `13.74` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `0.4877` n `228`; crypto_major avg `0.1834` n `8`; equity avg `0.3566` n `65`; fx avg `-0.0025` n `4`; index avg `0.1687` n `23`; metal avg `-0.018` n `18`; unknown avg `0.1183` n `356`
- 1h: commodity avg `-0.1173` n `12`; crypto_alt avg `-0.2111` n `228`; crypto_major avg `-0.3335` n `8`; equity avg `0.2418` n `65`; fx avg `-0.0054` n `4`; index avg `0.0423` n `23`; metal avg `0.2885` n `18`; unknown avg `1.5052` n `356`
- 4h: commodity avg `0.4588` n `7`; crypto_alt avg `-1.1809` n `223`; crypto_major avg `-1.2841` n `7`; equity avg `-0.9642` n `47`; fx avg `0.0618` n `4`; index avg `-0.48` n `6`; metal avg `-0.0915` n `7`; unknown avg `8.3045` n `313`
- 24h: commodity avg `-2.6423` n `7`; crypto_alt avg `2.4108` n `223`; crypto_major avg `1.0232` n `7`; equity avg `1.7612` n `47`; fx avg `-0.6184` n `4`; index avg `1.9312` n `6`; metal avg `2.6589` n `7`; unknown avg `19.4602` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1628`, n `458`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1569`, n `458`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `458`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `458`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `458`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `458`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `454`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `454`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0857`, n `458`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `454`, weak_sample_signal
