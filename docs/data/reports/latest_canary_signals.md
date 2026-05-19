# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T19:22:15.902731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0328` n `228`; crypto_major avg `0.007` n `8`; equity avg `0.0966` n `66`; fx avg `0.002` n `6`; index avg `0.0078` n `23`; metal avg `-0.0394` n `18`; unknown avg `-0.0275` n `383`
- 1h: commodity avg `0.2581` n `12`; crypto_alt avg `-0.1237` n `228`; crypto_major avg `0.0254` n `8`; equity avg `-0.2908` n `66`; fx avg `-0.0011` n `6`; index avg `-0.3353` n `23`; metal avg `-0.0549` n `18`; unknown avg `0.0827` n `383`
- 4h: commodity avg `0.5345` n `12`; crypto_alt avg `0.5931` n `228`; crypto_major avg `0.3595` n `8`; equity avg `1.2929` n `66`; fx avg `-0.014` n `6`; index avg `0.7049` n `23`; metal avg `-0.0735` n `18`; unknown avg `1.5686` n `383`
- 24h: commodity avg `1.2654` n `12`; crypto_alt avg `0.6262` n `228`; crypto_major avg `0.722` n `8`; equity avg `0.9992` n `66`; fx avg `0.0515` n `6`; index avg `0.0006` n `23`; metal avg `-2.2531` n `18`; unknown avg `1.4401` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
