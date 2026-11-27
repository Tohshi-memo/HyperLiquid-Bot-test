# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T04:07:26.949408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0545` n `13`; crypto_alt avg `-0.0782` n `239`; crypto_major avg `-0.0919` n `8`; equity avg `-0.0252` n `168`; fx avg `-0.0031` n `6`; index avg `0.0017` n `27`; metal avg `-0.0119` n `20`; unknown avg `-0.0951` n `1243`
- 1h: commodity avg `0.0607` n `13`; crypto_alt avg `-0.231` n `239`; crypto_major avg `-0.0718` n `8`; equity avg `0.4107` n `168`; fx avg `-0.0441` n `6`; index avg `0.0522` n `27`; metal avg `-0.0362` n `20`; unknown avg `66.8434` n `1251`
- 4h: commodity avg `0.1979` n `13`; crypto_alt avg `1.3689` n `239`; crypto_major avg `2.0019` n `8`; equity avg `2.5904` n `168`; fx avg `-0.0477` n `6`; index avg `0.2453` n `27`; metal avg `0.9019` n `20`; unknown avg `31.4216` n `1243`
- 24h: commodity avg `0.2209` n `13`; crypto_alt avg `1.4974` n `239`; crypto_major avg `1.5749` n `8`; equity avg `2.083` n `168`; fx avg `0.0361` n `6`; index avg `0.2266` n `27`; metal avg `0.7185` n `20`; unknown avg `203.5539` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
