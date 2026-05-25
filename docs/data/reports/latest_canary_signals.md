# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T18:52:19.811868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.0074` n `228`; crypto_major avg `-0.15` n `8`; equity avg `0.0179` n `67`; fx avg `0.0011` n `6`; index avg `0.0083` n `23`; metal avg `0.0117` n `18`; unknown avg `0.115` n `405`
- 1h: commodity avg `0.3798` n `12`; crypto_alt avg `-0.0304` n `228`; crypto_major avg `-0.1207` n `8`; equity avg `0.0098` n `67`; fx avg `0.0118` n `6`; index avg `0.01` n `23`; metal avg `0.0416` n `18`; unknown avg `-0.1141` n `405`
- 4h: commodity avg `0.0243` n `12`; crypto_alt avg `0.3265` n `228`; crypto_major avg `-0.4327` n `8`; equity avg `0.026` n `67`; fx avg `-0.013` n `6`; index avg `0.1498` n `23`; metal avg `0.3416` n `18`; unknown avg `-0.1424` n `405`
- 24h: commodity avg `-0.8546` n `12`; crypto_alt avg `2.3648` n `228`; crypto_major avg `0.472` n `8`; equity avg `0.9348` n `67`; fx avg `-0.0155` n `6`; index avg `0.5635` n `23`; metal avg `1.5879` n `18`; unknown avg `1.3103` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
