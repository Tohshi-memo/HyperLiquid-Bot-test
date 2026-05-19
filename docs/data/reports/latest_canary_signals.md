# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T17:37:19.991468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1861` n `12`; crypto_alt avg `-0.2326` n `228`; crypto_major avg `-0.2044` n `8`; equity avg `-0.029` n `66`; fx avg `0.0044` n `6`; index avg `-0.0596` n `23`; metal avg `-0.1721` n `18`; unknown avg `0.1945` n `383`
- 1h: commodity avg `-0.0739` n `12`; crypto_alt avg `0.2349` n `228`; crypto_major avg `0.2377` n `8`; equity avg `0.8123` n `66`; fx avg `0.0446` n `6`; index avg `0.3947` n `23`; metal avg `0.0518` n `18`; unknown avg `0.2056` n `383`
- 4h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.3851` n `228`; crypto_major avg `-0.1908` n `8`; equity avg `0.8837` n `66`; fx avg `-0.0378` n `6`; index avg `0.2458` n `23`; metal avg `0.3641` n `18`; unknown avg `-0.3004` n `383`
- 24h: commodity avg `0.5397` n `12`; crypto_alt avg `0.8147` n `228`; crypto_major avg `0.979` n `8`; equity avg `1.2479` n `66`; fx avg `-0.0045` n `6`; index avg `0.0961` n `23`; metal avg `-1.8587` n `18`; unknown avg `0.1801` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
