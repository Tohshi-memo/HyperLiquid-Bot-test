# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T09:07:21.446074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2257` n `12`; crypto_alt avg `-0.0905` n `228`; crypto_major avg `-0.0238` n `8`; equity avg `0.0893` n `67`; fx avg `-0.0126` n `6`; index avg `-0.0148` n `23`; metal avg `0.0551` n `18`; unknown avg `0.0693` n `419`
- 1h: commodity avg `-0.3014` n `12`; crypto_alt avg `-0.5349` n `228`; crypto_major avg `-0.4543` n `8`; equity avg `0.0096` n `67`; fx avg `-0.0061` n `6`; index avg `-0.0353` n `23`; metal avg `-0.1032` n `18`; unknown avg `-0.1374` n `419`
- 4h: commodity avg `-0.7155` n `12`; crypto_alt avg `-0.2887` n `228`; crypto_major avg `-0.0308` n `8`; equity avg `1.3486` n `67`; fx avg `0.0382` n `6`; index avg `0.498` n `23`; metal avg `0.9154` n `18`; unknown avg `0.026` n `409`
- 24h: commodity avg `0.4349` n `12`; crypto_alt avg `-4.8725` n `228`; crypto_major avg `-3.7268` n `8`; equity avg `-1.268` n `67`; fx avg `-0.0999` n `6`; index avg `-0.9224` n `23`; metal avg `-1.5982` n `18`; unknown avg `-1.7853` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
