# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T12:07:19.150175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1795` n `12`; crypto_alt avg `-0.1307` n `228`; crypto_major avg `-0.0572` n `8`; equity avg `0.0904` n `67`; fx avg `0.0191` n `6`; index avg `0.0696` n `23`; metal avg `0.1644` n `18`; unknown avg `-0.0826` n `419`
- 1h: commodity avg `0.1443` n `12`; crypto_alt avg `-0.0826` n `228`; crypto_major avg `0.0017` n `8`; equity avg `0.3221` n `67`; fx avg `0.0534` n `6`; index avg `0.1347` n `23`; metal avg `-0.1597` n `18`; unknown avg `-0.4897` n `419`
- 4h: commodity avg `0.2782` n `12`; crypto_alt avg `-0.9733` n `228`; crypto_major avg `-0.4885` n `8`; equity avg `-0.1504` n `67`; fx avg `0.0154` n `6`; index avg `-0.1101` n `23`; metal avg `-0.5161` n `18`; unknown avg `-0.4315` n `419`
- 24h: commodity avg `0.4606` n `12`; crypto_alt avg `-5.0589` n `228`; crypto_major avg `-3.6119` n `8`; equity avg `-1.6882` n `67`; fx avg `-0.0539` n `6`; index avg `-1.0997` n `23`; metal avg `-1.1695` n `18`; unknown avg `-1.8369` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
