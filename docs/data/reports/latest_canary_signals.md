# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T21:22:17.155805+00:00`
- Correlation status: `ready`
- Asset price records: `585`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1451` n `12`; crypto_alt avg `0.1908` n `228`; crypto_major avg `0.1349` n `8`; equity avg `-0.0202` n `65`; fx avg `0.0125` n `5`; index avg `-0.0221` n `23`; metal avg `-0.0348` n `18`; unknown avg `0.0213` n `365`
- 1h: commodity avg `1.1229` n `12`; crypto_alt avg `-0.5779` n `228`; crypto_major avg `-0.2447` n `8`; equity avg `-0.2374` n `65`; fx avg `-0.0275` n `5`; index avg `-0.0924` n `23`; metal avg `-0.7938` n `18`; unknown avg `-0.1484` n `365`
- 4h: commodity avg `1.1704` n `12`; crypto_alt avg `0.3492` n `228`; crypto_major avg `-0.0011` n `8`; equity avg `-0.1261` n `65`; fx avg `-0.0514` n `5`; index avg `-0.0467` n `23`; metal avg `-0.7338` n `18`; unknown avg `-0.2599` n `365`
- 24h: commodity avg `1.3368` n `12`; crypto_alt avg `0.8368` n `228`; crypto_major avg `-1.9713` n `8`; equity avg `-1.1954` n `65`; fx avg `0.1658` n `5`; index avg `-0.8054` n `23`; metal avg `-0.4181` n `18`; unknown avg `-0.4858` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `581`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `581`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `581`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `581`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `577`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `577`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.087`, n `577`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.084`, n `577`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0829`, n `577`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0807`, n `577`, weak_sample_signal
