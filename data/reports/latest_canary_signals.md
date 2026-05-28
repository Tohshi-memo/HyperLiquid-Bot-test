# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T07:37:15.741880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.2208` n `228`; crypto_major avg `0.1899` n `8`; equity avg `-0.0129` n `67`; fx avg `-0.0102` n `6`; index avg `-0.0304` n `23`; metal avg `-0.0859` n `18`; unknown avg `1.0497` n `419`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `1.0695` n `228`; crypto_major avg `0.9617` n `8`; equity avg `0.2441` n `67`; fx avg `0.0383` n `6`; index avg `0.1177` n `23`; metal avg `0.2114` n `18`; unknown avg `1.419` n `419`
- 4h: commodity avg `-0.332` n `12`; crypto_alt avg `-0.6677` n `228`; crypto_major avg `0.0796` n `8`; equity avg `0.8018` n `67`; fx avg `-0.0139` n `6`; index avg `0.2425` n `23`; metal avg `0.5764` n `18`; unknown avg `0.8114` n `409`
- 24h: commodity avg `0.2821` n `12`; crypto_alt avg `-4.4991` n `228`; crypto_major avg `-3.347` n `8`; equity avg `-1.1853` n `67`; fx avg `-0.1137` n `6`; index avg `-0.8767` n `23`; metal avg `-1.3001` n `18`; unknown avg `-0.9892` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
