# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T06:37:15.915701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.0799` n `228`; crypto_major avg `-0.0477` n `8`; equity avg `-0.036` n `66`; fx avg `-0.0303` n `6`; index avg `-0.0564` n `23`; metal avg `-0.1126` n `18`; unknown avg `-0.0662` n `384`
- 1h: commodity avg `-0.2005` n `12`; crypto_alt avg `0.0145` n `228`; crypto_major avg `0.0682` n `8`; equity avg `0.2481` n `66`; fx avg `-0.0342` n `6`; index avg `0.0758` n `23`; metal avg `0.0514` n `18`; unknown avg `-0.1648` n `374`
- 4h: commodity avg `-0.3469` n `12`; crypto_alt avg `0.8922` n `228`; crypto_major avg `0.8778` n `8`; equity avg `0.5587` n `66`; fx avg `-0.0213` n `6`; index avg `0.2556` n `23`; metal avg `0.6668` n `18`; unknown avg `0.2876` n `374`
- 24h: commodity avg `0.1786` n `12`; crypto_alt avg `-0.3345` n `228`; crypto_major avg `-0.108` n `8`; equity avg `0.4299` n `66`; fx avg `-0.1866` n `6`; index avg `-0.4335` n `23`; metal avg `-1.6661` n `18`; unknown avg `0.1049` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
