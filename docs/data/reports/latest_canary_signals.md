# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T09:37:17.171905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0683` n `228`; crypto_major avg `0.1062` n `8`; equity avg `0.062` n `66`; fx avg `-0.0033` n `6`; index avg `0.0335` n `23`; metal avg `0.0537` n `18`; unknown avg `0.7994` n `384`
- 1h: commodity avg `-0.1249` n `12`; crypto_alt avg `0.1449` n `228`; crypto_major avg `0.1608` n `8`; equity avg `0.0232` n `66`; fx avg `-0.0084` n `6`; index avg `0.0221` n `23`; metal avg `0.071` n `18`; unknown avg `0.6082` n `384`
- 4h: commodity avg `-0.5576` n `12`; crypto_alt avg `0.3984` n `228`; crypto_major avg `0.4042` n `8`; equity avg `0.7002` n `66`; fx avg `-0.0577` n `6`; index avg `0.3858` n `23`; metal avg `0.5396` n `18`; unknown avg `0.5526` n `374`
- 24h: commodity avg `-0.2262` n `12`; crypto_alt avg `0.842` n `228`; crypto_major avg `0.6698` n `8`; equity avg `1.3686` n `66`; fx avg `-0.1266` n `6`; index avg `0.1793` n `23`; metal avg `-0.7872` n `18`; unknown avg `0.1677` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
