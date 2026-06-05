# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T18:07:24.121502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6241` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `0.284` n `228`; crypto_major avg `0.2896` n `8`; equity avg `-0.2519` n `74`; fx avg `-0.0133` n `6`; index avg `-0.1098` n `23`; metal avg `-0.1492` n `18`; unknown avg `1.0503` n `424`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.4581` n `228`; crypto_major avg `-0.718` n `8`; equity avg `-0.3684` n `74`; fx avg `-0.0329` n `6`; index avg `-0.3859` n `23`; metal avg `-0.328` n `18`; unknown avg `0.6025` n `424`
- 4h: commodity avg `-0.7033` n `12`; crypto_alt avg `-0.1623` n `228`; crypto_major avg `-0.682` n `8`; equity avg `-2.3061` n `74`; fx avg `-0.1452` n `6`; index avg `-1.4038` n `23`; metal avg `-1.3798` n `18`; unknown avg `0.5111` n `424`
- 24h: commodity avg `-1.423` n `12`; crypto_alt avg `-7.1006` n `228`; crypto_major avg `-5.7635` n `8`; equity avg `-6.4391` n `74`; fx avg `-0.0687` n `6`; index avg `-3.6676` n `23`; metal avg `-4.205` n `18`; unknown avg `-1.636` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
