# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T13:37:34.927729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2664` n `12`; crypto_alt avg `-0.3434` n `228`; crypto_major avg `-0.2526` n `8`; equity avg `-0.5756` n `74`; fx avg `0.0243` n `6`; index avg `-0.0572` n `23`; metal avg `-0.0507` n `18`; unknown avg `-0.0473` n `643`
- 1h: commodity avg `0.1458` n `12`; crypto_alt avg `-0.4997` n `228`; crypto_major avg `-0.2821` n `8`; equity avg `-0.8384` n `74`; fx avg `0.0171` n `6`; index avg `-0.1062` n `23`; metal avg `0.1644` n `18`; unknown avg `-0.0249` n `643`
- 4h: commodity avg `0.944` n `12`; crypto_alt avg `-0.7679` n `228`; crypto_major avg `-0.4217` n `8`; equity avg `-1.3498` n `74`; fx avg `0.0131` n `6`; index avg `-0.3354` n `23`; metal avg `-0.6815` n `18`; unknown avg `1.1046` n `643`
- 24h: commodity avg `-1.8306` n `12`; crypto_alt avg `1.4715` n `228`; crypto_major avg `1.8465` n `8`; equity avg `2.1204` n `74`; fx avg `0.0058` n `6`; index avg `1.5865` n `23`; metal avg `2.6928` n `18`; unknown avg `1.7535` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
