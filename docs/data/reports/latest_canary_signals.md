# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T21:52:21.785840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2823` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0668` n `12`; crypto_alt avg `-1.3249` n `228`; crypto_major avg `-0.7538` n `8`; equity avg `-0.0401` n `67`; fx avg `-0.0025` n `6`; index avg `-0.036` n `23`; metal avg `-0.0398` n `18`; unknown avg `0.6288` n `419`
- 1h: commodity avg `0.1003` n `12`; crypto_alt avg `-1.9873` n `228`; crypto_major avg `-1.3126` n `8`; equity avg `-0.1692` n `67`; fx avg `-0.0002` n `6`; index avg `-0.0303` n `23`; metal avg `-0.0503` n `18`; unknown avg `0.6863` n `419`
- 4h: commodity avg `-0.1227` n `12`; crypto_alt avg `-1.6276` n `228`; crypto_major avg `-0.8064` n `8`; equity avg `0.2533` n `67`; fx avg `0.0108` n `6`; index avg `0.1765` n `23`; metal avg `0.024` n `18`; unknown avg `-0.0683` n `418`
- 24h: commodity avg `-1.0085` n `12`; crypto_alt avg `-2.2375` n `228`; crypto_major avg `-1.2188` n `8`; equity avg `-0.2556` n `67`; fx avg `-0.0702` n `6`; index avg `-0.4554` n `23`; metal avg `-1.3257` n `18`; unknown avg `-0.4816` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
