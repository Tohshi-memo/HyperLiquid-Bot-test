# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T06:07:18.742570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.0788` n `228`; crypto_major avg `0.0076` n `8`; equity avg `0.1336` n `66`; fx avg `-0.0007` n `6`; index avg `0.0344` n `23`; metal avg `0.079` n `18`; unknown avg `0.0795` n `374`
- 1h: commodity avg `0.091` n `12`; crypto_alt avg `0.6073` n `228`; crypto_major avg `0.3777` n `8`; equity avg `0.2021` n `66`; fx avg `-0.0135` n `6`; index avg `0.0722` n `23`; metal avg `0.1973` n `18`; unknown avg `0.2873` n `374`
- 4h: commodity avg `0.1917` n `12`; crypto_alt avg `0.9808` n `228`; crypto_major avg `0.6175` n `8`; equity avg `0.0643` n `66`; fx avg `0.0406` n `6`; index avg `-0.0578` n `23`; metal avg `0.1062` n `18`; unknown avg `0.2746` n `374`
- 24h: commodity avg `0.5628` n `12`; crypto_alt avg `-0.0952` n `228`; crypto_major avg `-0.2008` n `8`; equity avg `0.4184` n `66`; fx avg `-0.1595` n `6`; index avg `-0.4261` n `23`; metal avg `-1.7003` n `18`; unknown avg `1.0741` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
