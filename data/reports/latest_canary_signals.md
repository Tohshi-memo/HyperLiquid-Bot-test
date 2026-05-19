# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T21:37:17.328464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0684` n `12`; crypto_alt avg `0.0067` n `228`; crypto_major avg `-0.0882` n `8`; equity avg `0.0865` n `66`; fx avg `0.002` n `6`; index avg `0.0369` n `23`; metal avg `0.0312` n `18`; unknown avg `-0.0545` n `383`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.1389` n `228`; crypto_major avg `-0.0205` n `8`; equity avg `0.0759` n `66`; fx avg `-0.0333` n `6`; index avg `0.0657` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.0284` n `383`
- 4h: commodity avg `0.2105` n `12`; crypto_alt avg `0.0701` n `228`; crypto_major avg `-0.2492` n `8`; equity avg `-0.6631` n `66`; fx avg `0.0106` n `6`; index avg `-0.3517` n `23`; metal avg `-0.4711` n `18`; unknown avg `0.9677` n `383`
- 24h: commodity avg `1.0615` n `12`; crypto_alt avg `-0.4106` n `228`; crypto_major avg `-0.6325` n `8`; equity avg `-0.0406` n `66`; fx avg `0.0713` n `6`; index avg `-0.6781` n `23`; metal avg `-2.7006` n `18`; unknown avg `0.6074` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
