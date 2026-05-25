# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T14:52:17.850899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1552` n `12`; crypto_alt avg `0.0557` n `228`; crypto_major avg `-0.0627` n `8`; equity avg `0.0547` n `67`; fx avg `0.0091` n `6`; index avg `-0.0087` n `23`; metal avg `-0.244` n `18`; unknown avg `-0.0688` n `405`
- 1h: commodity avg `-0.3195` n `12`; crypto_alt avg `0.4744` n `228`; crypto_major avg `0.1963` n `8`; equity avg `0.1463` n `67`; fx avg `0.0004` n `6`; index avg `-0.0241` n `23`; metal avg `0.2594` n `18`; unknown avg `0.008` n `405`
- 4h: commodity avg `0.2652` n `12`; crypto_alt avg `0.4243` n `228`; crypto_major avg `0.2227` n `8`; equity avg `0.1154` n `67`; fx avg `0.0191` n `6`; index avg `0.0525` n `23`; metal avg `0.0031` n `18`; unknown avg `-0.1633` n `397`
- 24h: commodity avg `-0.7913` n `12`; crypto_alt avg `2.2323` n `228`; crypto_major avg `1.0176` n `8`; equity avg `0.9503` n `67`; fx avg `0.0029` n `6`; index avg `0.358` n `23`; metal avg `1.283` n `18`; unknown avg `0.7612` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
