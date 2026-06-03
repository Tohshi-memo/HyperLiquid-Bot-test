# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T22:22:26.241083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.567` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0554` n `12`; crypto_alt avg `-0.5565` n `228`; crypto_major avg `-0.5118` n `8`; equity avg `-0.0631` n `73`; fx avg `0.0048` n `6`; index avg `0.0043` n `23`; metal avg `-0.147` n `18`; unknown avg `-0.281` n `419`
- 1h: commodity avg `-0.2788` n `12`; crypto_alt avg `0.717` n `228`; crypto_major avg `0.3063` n `8`; equity avg `-0.1115` n `73`; fx avg `-0.0046` n `6`; index avg `-0.1403` n `23`; metal avg `-0.2364` n `18`; unknown avg `0.8599` n `419`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.3397` n `228`; crypto_major avg `0.036` n `8`; equity avg `-1.531` n `73`; fx avg `0.0012` n `6`; index avg `-0.469` n `23`; metal avg `-0.4472` n `18`; unknown avg `0.8249` n `419`
- 24h: commodity avg `0.6429` n `12`; crypto_alt avg `1.4083` n `228`; crypto_major avg `-1.1521` n `8`; equity avg `-3.5273` n `72`; fx avg `0.0388` n `6`; index avg `-0.8747` n `23`; metal avg `-2.4842` n `18`; unknown avg `0.4665` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
