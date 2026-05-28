# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T09:52:23.629601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1797` n `12`; crypto_alt avg `0.2377` n `228`; crypto_major avg `0.1456` n `8`; equity avg `0.0472` n `67`; fx avg `0.0029` n `6`; index avg `0.0081` n `23`; metal avg `0.0348` n `18`; unknown avg `0.1111` n `419`
- 1h: commodity avg `-0.2169` n `12`; crypto_alt avg `0.3351` n `228`; crypto_major avg `0.3398` n `8`; equity avg `0.049` n `67`; fx avg `-0.0191` n `6`; index avg `-0.0316` n `23`; metal avg `0.083` n `18`; unknown avg `0.1671` n `419`
- 4h: commodity avg `-0.5266` n `12`; crypto_alt avg `0.6037` n `228`; crypto_major avg `0.5382` n `8`; equity avg `0.4301` n `67`; fx avg `0.0143` n `6`; index avg `0.1801` n `23`; metal avg `0.1251` n `18`; unknown avg `0.2136` n `409`
- 24h: commodity avg `0.4247` n `12`; crypto_alt avg `-4.2993` n `228`; crypto_major avg `-3.5362` n `8`; equity avg `-1.5067` n `67`; fx avg `-0.097` n `6`; index avg `-1.0026` n `23`; metal avg `-1.6918` n `18`; unknown avg `-1.4535` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
