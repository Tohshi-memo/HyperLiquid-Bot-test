# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T21:22:33.633741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0365` n `239`; crypto_major avg `-0.06` n `8`; equity avg `0.0291` n `168`; fx avg `-0.0034` n `6`; index avg `0.007` n `27`; metal avg `-0.0058` n `20`; unknown avg `4.5362` n `1219`
- 1h: commodity avg `0.0076` n `13`; crypto_alt avg `0.2322` n `239`; crypto_major avg `0.0525` n `8`; equity avg `0.1244` n `168`; fx avg `0.003` n `6`; index avg `0.026` n `27`; metal avg `0.0243` n `20`; unknown avg `1.3614` n `1183`
- 4h: commodity avg `0.0272` n `13`; crypto_alt avg `0.2459` n `239`; crypto_major avg `-0.0541` n `8`; equity avg `0.5708` n `168`; fx avg `-0.0168` n `6`; index avg `0.0624` n `27`; metal avg `0.2381` n `20`; unknown avg `179.5006` n `1162`
- 24h: commodity avg `-0.4848` n `13`; crypto_alt avg `-0.0457` n `239`; crypto_major avg `-0.2047` n `8`; equity avg `3.1585` n `168`; fx avg `-0.1531` n `6`; index avg `0.3167` n `27`; metal avg `0.9493` n `20`; unknown avg `275.2594` n `1003`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
