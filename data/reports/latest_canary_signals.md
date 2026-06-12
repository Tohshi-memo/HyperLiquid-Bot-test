# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T15:52:33.816792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1061` n `12`; crypto_alt avg `-0.2425` n `228`; crypto_major avg `-0.3541` n `8`; equity avg `-0.3911` n `74`; fx avg `0.0` n `6`; index avg `-0.1669` n `23`; metal avg `-0.1674` n `18`; unknown avg `0.0959` n `643`
- 1h: commodity avg `-0.5075` n `12`; crypto_alt avg `-0.3849` n `228`; crypto_major avg `-0.3967` n `8`; equity avg `-0.2011` n `74`; fx avg `0.0079` n `6`; index avg `0.2047` n `23`; metal avg `0.4864` n `18`; unknown avg `-0.3433` n `643`
- 4h: commodity avg `0.1221` n `12`; crypto_alt avg `-0.0929` n `228`; crypto_major avg `0.387` n `8`; equity avg `-1.0331` n `74`; fx avg `-0.0032` n `6`; index avg `0.0687` n `23`; metal avg `-0.1998` n `18`; unknown avg `13.9148` n `643`
- 24h: commodity avg `-2.354` n `12`; crypto_alt avg `1.7938` n `228`; crypto_major avg `2.6534` n `8`; equity avg `2.0213` n `74`; fx avg `0.0848` n `6`; index avg `1.7268` n `23`; metal avg `2.6531` n `18`; unknown avg `20.7242` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
