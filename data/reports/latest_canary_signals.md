# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T18:22:31.552742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `12`; crypto_alt avg `-0.7046` n `228`; crypto_major avg `-0.524` n `8`; equity avg `0.0235` n `73`; fx avg `-0.0269` n `6`; index avg `-0.0134` n `23`; metal avg `-0.026` n `18`; unknown avg `-0.1529` n `419`
- 1h: commodity avg `-0.1971` n `12`; crypto_alt avg `-0.1406` n `228`; crypto_major avg `0.042` n `8`; equity avg `0.4374` n `73`; fx avg `-0.0132` n `6`; index avg `0.0809` n `23`; metal avg `-0.1752` n `18`; unknown avg `-0.1946` n `419`
- 4h: commodity avg `0.4313` n `12`; crypto_alt avg `-1.0133` n `228`; crypto_major avg `-0.8272` n `8`; equity avg `-0.6459` n `73`; fx avg `-0.0172` n `6`; index avg `-0.0905` n `23`; metal avg `-0.573` n `18`; unknown avg `-0.4596` n `419`
- 24h: commodity avg `0.8038` n `12`; crypto_alt avg `0.2671` n `228`; crypto_major avg `-2.5544` n `8`; equity avg `-1.7465` n `72`; fx avg `0.0426` n `6`; index avg `-0.1505` n `23`; metal avg `-1.9712` n `18`; unknown avg `0.4386` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
