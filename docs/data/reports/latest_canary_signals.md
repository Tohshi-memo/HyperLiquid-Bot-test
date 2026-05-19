# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T16:22:16.911120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0343` n `12`; crypto_alt avg `0.0333` n `228`; crypto_major avg `0.0127` n `8`; equity avg `0.0124` n `66`; fx avg `-0.0684` n `6`; index avg `0.0736` n `23`; metal avg `-0.0451` n `18`; unknown avg `-0.1` n `383`
- 1h: commodity avg `0.1888` n `12`; crypto_alt avg `0.1786` n `228`; crypto_major avg `0.0445` n `8`; equity avg `0.3998` n `66`; fx avg `-0.0685` n `6`; index avg `0.2496` n `23`; metal avg `0.0508` n `18`; unknown avg `-0.0628` n `383`
- 4h: commodity avg `0.1998` n `12`; crypto_alt avg `-0.4287` n `228`; crypto_major avg `-0.1533` n `8`; equity avg `0.3146` n `66`; fx avg `-0.0959` n `6`; index avg `-0.1722` n `23`; metal avg `-1.2696` n `18`; unknown avg `-0.2781` n `383`
- 24h: commodity avg `0.6843` n `12`; crypto_alt avg `0.3937` n `228`; crypto_major avg `0.6966` n `8`; equity avg `-0.4418` n `66`; fx avg `-0.0277` n `6`; index avg `-0.7436` n `23`; metal avg `-1.9908` n `18`; unknown avg `-0.0766` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
