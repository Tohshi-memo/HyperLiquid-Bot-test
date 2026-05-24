# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T16:07:15.802314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1102` n `12`; crypto_alt avg `0.1578` n `228`; crypto_major avg `0.1434` n `8`; equity avg `0.0579` n `67`; fx avg `0.0127` n `6`; index avg `-0.0096` n `23`; metal avg `0.0203` n `18`; unknown avg `0.0782` n `396`
- 1h: commodity avg `-0.4346` n `12`; crypto_alt avg `0.4227` n `228`; crypto_major avg `0.3138` n `8`; equity avg `-0.0517` n `67`; fx avg `0.0124` n `6`; index avg `-0.0564` n `23`; metal avg `0.1639` n `18`; unknown avg `-0.2527` n `396`
- 4h: commodity avg `0.6169` n `12`; crypto_alt avg `-0.5812` n `228`; crypto_major avg `-0.5436` n `8`; equity avg `-0.3376` n `67`; fx avg `0.0371` n `6`; index avg `-0.3875` n `23`; metal avg `-0.4414` n `18`; unknown avg `0.1203` n `396`
- 24h: commodity avg `-1.4012` n `12`; crypto_alt avg `0.8345` n `228`; crypto_major avg `2.3634` n `8`; equity avg `1.5524` n `67`; fx avg `0.0878` n `6`; index avg `0.566` n `23`; metal avg `0.6247` n `18`; unknown avg `0.9659` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
