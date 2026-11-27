# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T13:07:28.658034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0631` n `13`; crypto_alt avg `-0.0079` n `239`; crypto_major avg `0.0579` n `8`; equity avg `0.0688` n `168`; fx avg `-0.0184` n `6`; index avg `0.0165` n `27`; metal avg `0.0417` n `20`; unknown avg `0.4274` n `1247`
- 1h: commodity avg `-0.1851` n `13`; crypto_alt avg `-0.0366` n `239`; crypto_major avg `-0.1303` n `8`; equity avg `0.4696` n `168`; fx avg `-0.0149` n `6`; index avg `0.0695` n `27`; metal avg `-0.0408` n `20`; unknown avg `0.4495` n `1251`
- 4h: commodity avg `-0.3351` n `13`; crypto_alt avg `-0.1529` n `239`; crypto_major avg `-0.2879` n `8`; equity avg `-0.6306` n `168`; fx avg `0.0048` n `6`; index avg `-0.0391` n `27`; metal avg `-0.2832` n `20`; unknown avg `187.0872` n `1243`
- 24h: commodity avg `-0.2128` n `13`; crypto_alt avg `1.7292` n `239`; crypto_major avg `2.4244` n `8`; equity avg `3.3531` n `168`; fx avg `-0.0933` n `6`; index avg `0.2948` n `27`; metal avg `1.1072` n `20`; unknown avg `264.457` n `1023`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
