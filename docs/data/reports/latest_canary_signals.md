# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T01:07:12.038463+00:00`
- Correlation status: `ready`
- Asset price records: `504`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.4069` n `228`; crypto_major avg `-0.2821` n `8`; equity avg `-0.141` n `65`; fx avg `0.0173` n `4`; index avg `-0.0413` n `23`; metal avg `0.1089` n `18`; unknown avg `-0.1332` n `357`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `-0.971` n `228`; crypto_major avg `-0.7666` n `8`; equity avg `-0.3804` n `65`; fx avg `0.0334` n `4`; index avg `-0.0746` n `23`; metal avg `0.0758` n `18`; unknown avg `-0.159` n `356`
- 4h: commodity avg `0.0203` n `12`; crypto_alt avg `-0.998` n `228`; crypto_major avg `-0.8859` n `8`; equity avg `-0.3886` n `65`; fx avg `0.1021` n `4`; index avg `-0.0271` n `23`; metal avg `0.0596` n `18`; unknown avg `-0.1842` n `356`
- 24h: commodity avg `-1.672` n `7`; crypto_alt avg `1.1291` n `223`; crypto_major avg `-0.3646` n `7`; equity avg `1.3482` n `47`; fx avg `-0.238` n `4`; index avg `0.8668` n `6`; metal avg `2.3932` n `7`; unknown avg `3.2349` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1276`, n `500`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `500`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0726`, n `496`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `500`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0655`, n `496`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `500`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `496`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0578`, n `496`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0566`, n `496`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0555`, n `496`, weak_sample_signal
