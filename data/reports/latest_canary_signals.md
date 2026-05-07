# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T15:52:19.224814+00:00`
- Correlation status: `ready`
- Asset price records: `563`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3936` n `12`; crypto_alt avg `-0.1761` n `228`; crypto_major avg `-0.0989` n `8`; equity avg `-0.3465` n `65`; fx avg `0.0002` n `5`; index avg `-0.1792` n `23`; metal avg `-0.4253` n `18`; unknown avg `-0.0315` n `365`
- 1h: commodity avg `0.6966` n `12`; crypto_alt avg `-0.2534` n `228`; crypto_major avg `-0.2175` n `8`; equity avg `-0.5521` n `65`; fx avg `0.0468` n `5`; index avg `-0.1735` n `23`; metal avg `-0.8847` n `18`; unknown avg `-0.0927` n `365`
- 4h: commodity avg `0.6931` n `12`; crypto_alt avg `-0.7505` n `228`; crypto_major avg `-1.1788` n `8`; equity avg `-0.6358` n `65`; fx avg `0.0362` n `5`; index avg `-0.3743` n `23`; metal avg `-0.6215` n `18`; unknown avg `-0.2336` n `365`
- 24h: commodity avg `-0.4739` n `12`; crypto_alt avg `0.0391` n `228`; crypto_major avg `-2.075` n `8`; equity avg `0.4359` n `65`; fx avg `0.1491` n `5`; index avg `0.1972` n `23`; metal avg `1.0319` n `18`; unknown avg `-0.2091` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `559`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `559`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `559`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `559`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0876`, n `555`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `555`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `555`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0833`, n `555`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `559`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `559`, weak_sample_signal
