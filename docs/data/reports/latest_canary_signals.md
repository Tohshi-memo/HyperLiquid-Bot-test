# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T01:07:28.095532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0408` n `229`; crypto_major avg `-0.0024` n `8`; equity avg `0.0163` n `92`; fx avg `0.0011` n `6`; index avg `0.0001` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0351` n `765`
- 1h: commodity avg `0.0395` n `12`; crypto_alt avg `-0.0265` n `229`; crypto_major avg `-0.0809` n `8`; equity avg `-0.0152` n `92`; fx avg `-0.0043` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0026` n `20`; unknown avg `1.5272` n `765`
- 4h: commodity avg `0.0092` n `12`; crypto_alt avg `0.2389` n `229`; crypto_major avg `0.0682` n `8`; equity avg `0.0758` n `92`; fx avg `-0.0004` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0272` n `20`; unknown avg `1.3194` n `765`
- 24h: commodity avg `-0.2296` n `12`; crypto_alt avg `1.0944` n `229`; crypto_major avg `0.9725` n `8`; equity avg `-0.4677` n `92`; fx avg `-0.1638` n `6`; index avg `0.1069` n `25`; metal avg `0.0853` n `20`; unknown avg `1.0643` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
