# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T15:37:38.902008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `0.0185` n `228`; crypto_major avg `0.1727` n `8`; equity avg `-0.93` n `74`; fx avg `-0.0064` n `6`; index avg `0.0367` n `23`; metal avg `0.0084` n `18`; unknown avg `-0.0227` n `690`
- 1h: commodity avg `0.2037` n `12`; crypto_alt avg `-0.2338` n `228`; crypto_major avg `0.5303` n `8`; equity avg `-0.6342` n `74`; fx avg `0.0007` n `6`; index avg `0.1968` n `23`; metal avg `-0.0541` n `18`; unknown avg `0.1079` n `690`
- 4h: commodity avg `0.4228` n `12`; crypto_alt avg `0.4315` n `228`; crypto_major avg `1.1138` n `8`; equity avg `-0.1895` n `74`; fx avg `-0.0256` n `6`; index avg `0.3136` n `23`; metal avg `0.0235` n `18`; unknown avg `0.5025` n `689`
- 24h: commodity avg `-0.8898` n `12`; crypto_alt avg `5.9743` n `228`; crypto_major avg `6.6717` n `8`; equity avg `1.5861` n `74`; fx avg `0.058` n `6`; index avg `1.1639` n `23`; metal avg `2.8254` n `18`; unknown avg `2.4867` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
