# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T11:07:28.563664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0877` n `12`; crypto_alt avg `0.4171` n `228`; crypto_major avg `0.1275` n `8`; equity avg `0.0243` n `72`; fx avg `-0.0192` n `6`; index avg `0.0026` n `23`; metal avg `0.0923` n `18`; unknown avg `0.157` n `420`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.5543` n `228`; crypto_major avg `0.06` n `8`; equity avg `0.0334` n `72`; fx avg `-0.0071` n `6`; index avg `-0.0221` n `23`; metal avg `-0.0681` n `18`; unknown avg `-0.0957` n `420`
- 4h: commodity avg `0.4516` n `12`; crypto_alt avg `1.0417` n `228`; crypto_major avg `0.3057` n `8`; equity avg `-0.1167` n `72`; fx avg `-0.0011` n `6`; index avg `-0.0271` n `23`; metal avg `0.0025` n `18`; unknown avg `0.1646` n `420`
- 24h: commodity avg `1.8185` n `12`; crypto_alt avg `-0.5386` n `228`; crypto_major avg `-3.0396` n `8`; equity avg `0.7708` n `72`; fx avg `0.0381` n `6`; index avg `0.93` n `23`; metal avg `-1.2825` n `18`; unknown avg `-0.2316` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
