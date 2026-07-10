# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T22:52:31.712746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0355` n `229`; crypto_major avg `-0.0098` n `8`; equity avg `-0.0006` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.062` n `765`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.0643` n `229`; crypto_major avg `0.0667` n `8`; equity avg `-0.0049` n `92`; fx avg `-0.0312` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0873` n `765`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.633` n `229`; crypto_major avg `0.3991` n `8`; equity avg `-0.0528` n `92`; fx avg `-0.0336` n `6`; index avg `0.0073` n `25`; metal avg `0.1128` n `20`; unknown avg `-0.2468` n `765`
- 24h: commodity avg `-0.2424` n `12`; crypto_alt avg `1.0713` n `229`; crypto_major avg `0.9283` n `8`; equity avg `-0.7397` n `92`; fx avg `-0.2003` n `6`; index avg `0.0186` n `25`; metal avg `0.1499` n `20`; unknown avg `-0.2572` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
