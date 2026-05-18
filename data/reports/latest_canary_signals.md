# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T08:39:46.634278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0675` n `12`; crypto_alt avg `-0.0529` n `228`; crypto_major avg `-0.0588` n `8`; equity avg `0.099` n `66`; fx avg `-0.0056` n `5`; index avg `0.074` n `23`; metal avg `0.1344` n `18`; unknown avg `-0.0707` n `383`
- 1h: commodity avg `0.1606` n `12`; crypto_alt avg `-0.0014` n `228`; crypto_major avg `0.0043` n `8`; equity avg `0.4779` n `66`; fx avg `-0.0075` n `5`; index avg `0.2181` n `23`; metal avg `0.0486` n `18`; unknown avg `-0.2765` n `383`
- 4h: commodity avg `-0.2577` n `12`; crypto_alt avg `-0.681` n `228`; crypto_major avg `-0.4219` n `8`; equity avg `0.8595` n `66`; fx avg `-0.0773` n `5`; index avg `0.3203` n `23`; metal avg `0.5033` n `18`; unknown avg `-0.2665` n `363`
- 24h: commodity avg `0.627` n `12`; crypto_alt avg `-2.9797` n `228`; crypto_major avg `-1.2862` n `8`; equity avg `0.5882` n `65`; fx avg `0.0251` n `5`; index avg `0.331` n `23`; metal avg `0.1965` n `18`; unknown avg `-0.4998` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
