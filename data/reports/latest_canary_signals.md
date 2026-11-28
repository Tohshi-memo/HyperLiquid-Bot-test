# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T06:22:26.718981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `0.2498` n `239`; crypto_major avg `0.1476` n `8`; equity avg `0.0073` n `168`; fx avg `-0.0019` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0049` n `20`; unknown avg `0.5218` n `1261`
- 1h: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.5258` n `239`; crypto_major avg `-0.0643` n `8`; equity avg `-0.1434` n `168`; fx avg `-0.0016` n `6`; index avg `-0.0151` n `27`; metal avg `-0.028` n `20`; unknown avg `0.4812` n `1231`
- 4h: commodity avg `-0.0219` n `13`; crypto_alt avg `-1.8338` n `239`; crypto_major avg `-0.8443` n `8`; equity avg `-0.3049` n `168`; fx avg `0.0132` n `6`; index avg `-0.0373` n `27`; metal avg `-0.0421` n `20`; unknown avg `2.3115` n `1215`
- 24h: commodity avg `-0.8797` n `13`; crypto_alt avg `-3.1844` n `239`; crypto_major avg `-2.5983` n `8`; equity avg `-0.6141` n `168`; fx avg `-0.1521` n `6`; index avg `-0.0054` n `27`; metal avg `-0.2106` n `20`; unknown avg `215.9749` n `967`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
