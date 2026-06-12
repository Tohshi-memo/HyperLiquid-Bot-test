# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T17:22:30.863524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.2162` n `228`; crypto_major avg `-0.2234` n `8`; equity avg `0.1468` n `74`; fx avg `0.0005` n `6`; index avg `0.1025` n `23`; metal avg `0.0957` n `18`; unknown avg `-0.0087` n `643`
- 1h: commodity avg `0.042` n `12`; crypto_alt avg `0.1262` n `228`; crypto_major avg `0.2887` n `8`; equity avg `0.5672` n `74`; fx avg `0.0007` n `6`; index avg `0.2765` n `23`; metal avg `-0.0417` n `18`; unknown avg `-0.0713` n `643`
- 4h: commodity avg `0.066` n `12`; crypto_alt avg `-0.1749` n `228`; crypto_major avg `0.5565` n `8`; equity avg `0.3376` n `74`; fx avg `0.0049` n `6`; index avg `0.6094` n `23`; metal avg `0.407` n `18`; unknown avg `27.1726` n `643`
- 24h: commodity avg `-1.8323` n `12`; crypto_alt avg `2.2476` n `228`; crypto_major avg `3.3083` n `8`; equity avg `3.2234` n `74`; fx avg `0.0944` n `6`; index avg `2.2429` n `23`; metal avg `3.3357` n `18`; unknown avg `44.1905` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
